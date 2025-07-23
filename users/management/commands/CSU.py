from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    help = "Создание суперпользователя с email вместо username"

    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email="admin@mail.ru",
            phone_number="+1234567890",
            country="Russia",
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        user.set_password("qwer1234")
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f"Superuser created successfully: {user.email}")
        )