from django.urls import path

from .views import *

app_name = "User"

urlpatterns = [
    path('authenticate', entry, name="Entry"),
    path('login', login_view, name="Login"),
    path('logout', logout_view, name='Logout'),
    path('signup', signup, name='SignUp')
]
