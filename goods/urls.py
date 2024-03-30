from django.urls import path

from goods.views import catalog, product

app_name = 'goods'

urlpatterns = [
    path('', catalog, name='index'),
    path('product/<int:product_id>', product, name='product'),
]