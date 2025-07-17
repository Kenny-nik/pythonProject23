import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import CustomUser

load_dotenv()


class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.create(
            username="GGWP",
            email="admin@mail.ru",
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("qwer1234")
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Admin user created: {user.username}, {user.email}"
            )
        )