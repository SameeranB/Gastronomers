from django.urls import path, include, re_path
from .views import *

app_name = "Main"


urlpatterns = [
    path('', index, name="Index"),
    path('restaurant/<int:id>', restaurant_view, name="Restaurant"),
]