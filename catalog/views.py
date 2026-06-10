from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.order_by('-created_at')[:5]

    print('Последние 5 товаров:')
    for product in products:
        print(product)

    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')
