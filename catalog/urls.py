from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name
urlpatterns = [
    path('', views.ProductListView.as_view(), name='catalog_list'),
    # path('contacts/', views.ContactTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]