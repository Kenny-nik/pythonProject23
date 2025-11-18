from IPython.core.compilerop import code_name
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from parso.python.tree import Class

class Command(BaseCommand):
    help = 'создание группы "Модераторы"'
    def handle(self, *args, **options):
        moderators_group = Group.objects.create(name='moderators')
        publish_product = Permission.objects.get(codename='can_unpublish_product')
        delete_product = Permission.objects.get(codename='delete_product')


        moderators_group.permissions.add(publish_product, delete_product)
        moderators_group.save()
        self.stdout.write(self.style.SUCCSESS(f'группа "модераторы" создана'))