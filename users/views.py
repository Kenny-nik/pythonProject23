from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:catalog_list")
    template_name = "users/register.html"