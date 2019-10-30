from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from user.models import CustomUser


def entry(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("User Logged in")
            messages.success(request, 'You have been logged in successfully')
            return redirect('Feed:Feed')
        else:
            messages.error(request, 'Invalid authentication details')
            return redirect('User:Entry')

    else:
        return HttpResponse("Invalid Method")


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('Main:Index')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        name_parts = name.split(' ')

        first_name = name_parts[0]
        last_name = name_parts[1]

        user = CustomUser.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()

        login(request, user)
        print("User Logged in")
        messages.success(request, 'You have signed up successfully')
        return redirect('Feed:Feed')

