from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUsreAdmin(admin.ModelAdmin):
    exclude = ('password', )

