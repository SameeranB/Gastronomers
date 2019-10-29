from django.shortcuts import render


# Create your views here.
from main.models import Restaurant


def index(request):
    return render(request, 'index.html')


# def search(request):
#        search_word = request.data.get('search')
#        restaurants = Restaurant.objects.filter()

def restaurant_view(request, **kwargs):
    res = Restaurant.objects.get(restaurant_id=kwargs['id'])
    return render(request, 'restaurant.html', {'restaurant': res, 'n': range(res.rating)})