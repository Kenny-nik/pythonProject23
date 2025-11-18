from gc import get_objects
from itertools import product
from django.core.cache import cache
from django.db.transaction import commit
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm, ModeratorProductForm
from catalog.models import Product
from catalog.services import CategoryService


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return redirect(reverse('catalog:catalog_list'))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ModeratorProductForm


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete_confirm.html"
    success_url = reverse_lazy("catalog:catalog_list")
    context_object_name = "product"
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if request.user == product.owner or request.user.has_perm('catalog.delete_product'):
            product.delete()
            return redirect(reverse('catalog:catalog_list'))
        else:
            return HttpResponseForbidden('Недостаточно прав')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        cached_products=cache.get('products')
        if cached_products:
            return cached_products
        products = Product.objects.all()
        cache.set('products', products, 60*5)
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()
        return Product.objects.filter(is_published=True)


@method_decorator(cache_page(60*5), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ContactTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(name)
            print(phone)
            print(message)
            return HttpResponse('Сообщение отправлено!')


class ProductsByCategoryView(ListView):
    template_name = 'catalog/products_list.html'  # используем существующий шаблон
    context_object_name = 'products'

    def get_queryset(self):
        category = self.kwargs['pk']
        return CategoryService.get_from_categories(category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товары категории'  # можно доработать, добавив название категории
        return context