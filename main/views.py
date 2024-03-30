from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):
    
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context=context)

def view_about(request):
    context = {
        'title': 'HOME - О нас',
        'content': 'О нас',
        'text_on_page': 'Это очень хороший магазин!',
    }
    return render(request, 'main/about.html', context=context)