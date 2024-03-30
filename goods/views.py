from django.shortcuts import render

from .models import Products

# Create your views here.
def catalog(request):

    goods = Products.objects.all()
    
    context = {
        'title': 'Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request, product_id):
    product = Products.objects.get(id=product_id)

    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context=context)
