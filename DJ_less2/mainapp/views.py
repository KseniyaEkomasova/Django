from django.shortcuts import render
from django.http import HttpRequest
import datetime

def main(request: HttpRequest):
    content = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', content)

def product(request: HttpRequest):
    content = {
        'page_title': 'каталог',
    }
    return render(request, 'mainapp/product.html', content)

def contacts(request: HttpRequest):
    content = {
        'page_title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', content)

def today():
    return datetime.date.today()