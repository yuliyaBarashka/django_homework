from django.core.management import BaseCommand
from django.core.management import call_command

from catalog.models import Product, Category

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command(
            'loaddata',
            'catalog/fixtures/categories.json'
        )

        call_command(
            'loaddata',
            'catalog/fixtures/products.json'
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Данные загружены'
            )
        )
