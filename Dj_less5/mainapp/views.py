from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
import datetime
from .models import ProductCategory, Product
import json
from basketapp.models import Basket

def main(request: HttpRequest):

    content = {
        'page_title': 'главная',

    }
    return render(request, 'mainapp/index.html', content)

def product(request: HttpRequest, id=None):
    links_menu = ProductCategory.objects.all()
    if id is not None:
        products = Product.objects.filter(category__pk=id)
    else:
        products = Product.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if id:
        if id == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=id)
            products = Product.objects.filter(category__pk=pk).order_by('price')

    content = {
        'page_title': 'каталог',
        'links_menu': links_menu,
        'products': products,
        'basket': basket,
        'category': category,
    }
    return render(request, 'mainapp/product.html', content)

def product_detail(request:HttpRequest, id=None):
    if id is not None:
        #item = Product.objects.get(pk=id)
        item = get_object_or_404(Product, pk=id)
        products = Product.objects.exclude(pk=id).filter(category__pk=item.category_id)
        links_menu = ProductCategory.objects.all()

        content = {
            'title': f'Товар:{item.name}',
            'item': item,
            'products': products,
            'links_menu': links_menu,
        }

        return render(request, 'mainapp/details.html', content)

def contacts(request: HttpRequest):
    # locations = [
    #     {
    #         'city': 'Москва',
    #         'phone': '+78142332211',
    #         'email': 'ivai@yandex.ru',
    #         'address': 'Парк Останкино, офис 392',
    #     },
    #
    #     {
    #         'city': 'Нижний Новгород',
    #         'phone': '+78142332211',
    #         'email': 'ivai@yandex.ru',
    #         'address': 'Парк Горького',
    #     },
    #
    # ]
    #
    # with open('mainapp/json/locations.json', 'w', encoding='utf-8') as tmp_file:
    #     json.dump(locations, tmp_file)

    with open('mainapp/json/locations.json', 'r', encoding='utf-8') as tmp_file:
        locations = json.load(tmp_file)

    content = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contacts.html', content)

def today():
    return datetime.date.today()

def products_index(request: HttpRequest, id=None):
    pass