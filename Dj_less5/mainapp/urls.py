from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.product, name='index'),
   path('<int:id>/', mainapp.product, name='category'),
   path('details/<int:id>/', mainapp.product_detail, name='details'),
]
