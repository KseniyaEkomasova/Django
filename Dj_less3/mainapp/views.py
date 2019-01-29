from django.shortcuts import render
from django.http import HttpRequest
import datetime
from .models import ProductCategory, Product
import json

def main(request: HttpRequest):
    content = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', content)

def product(request: HttpRequest):
    products = Product.objects.all()
    content = {
        'page_title': 'каталог',
        'products': products,
    }
    return render(request, 'mainapp/product.html', content)

def contacts(request: HttpRequest):
    locations = [
        {
            'city': 'Москва',
            'phone': '+78142332211',
            'email': 'ivai@yandex.ru',
            'address': 'Парк Останкино, офис 392',
        },

        {
            'city': 'Нижний Новгород',
            'phone': '+78142332211',
            'email': 'ivai@yandex.ru',
            'address': 'Парк Горького',
        },

    ]

    with open('json/locations.json', 'w', encoding='utf-8') as tmp_file:
        json.dump(locations, tmp_file)

    content = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contacts.html', content)

def today():
    return datetime.date.today()

def products_index(request: HttpRequest, id=None):
    pass