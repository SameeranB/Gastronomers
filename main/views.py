from django.shortcuts import render


# Create your views here.
from main.models import Restaurant


def index(request):
    return render(request, 'index.html')


def search(request):
       search_word = request.data.get('search')
       restaurants = Restaurant.objects.filter()