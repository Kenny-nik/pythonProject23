from unicodedata import category

from .models import Category, Product


class CategoryService:
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_from_categories():
        return Product.objects.filter(category=category)