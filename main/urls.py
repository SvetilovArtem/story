from django.urls import path

from main.views import index, view_about

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', view_about, name='about'),
]