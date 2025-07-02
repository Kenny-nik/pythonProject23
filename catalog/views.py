# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.models import Product
# from .forms import ProductForm

class ProductCreateView(CreateView):
    model = Product
    fields = ("name","description","stock","category","image","price")
    success_url = reverse_lazy("catalog:catalog_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "stock", "category", "image", "price")
    success_url = reverse_lazy("catalog:catalog_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog_list")

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactDetailView(TemplateView):
    template_name = "catalog/contacts.html"


# class ContactTemplateView(TemplateView):
#     template_name = 'catalog/contacts.html'
#
#     def get_context_data(self, **kwargs):
#         if self.request.method == 'POST':
#             name = self.request.POST.get('name')
#             phone = self.request.POST.get('phone')
#             message = self.request.POST.get('message')
#             print(name)
#             print(phone)
#             print(message)
#             return HttpResponse('Сообщение отправлено!')


# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'catalog/product_form.html'
#     success_url = reverse_lazy('catalog:home')


# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'catalog/product_form.html'
#     success_url = reverse_lazy('catalog:home')
#
#
# class ProductDeleteView(DeleteView):
#     model = Product
#     template_name = 'catalog/product_delete_confirm.html'
#     success_url = reverse_lazy('catalog:home')
#     context_object_name = 'product'