from django.urls import path
from django.views.decorators.cache import cache_page
from .apps import CatalogConfig
from .views import (
    ProductListView,
    ProductDetailView,
    ContactTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name='catalog_list'),
    path("catalog/products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail",),
    path("catalog/contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product")
]