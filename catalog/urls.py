from django.urls import path
from . import views
from .apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name
urlpatterns = [
    path('', views.ProductListView.as_view(), name='catalog_list'),
    path('contacts/', views.ContactDetailView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]