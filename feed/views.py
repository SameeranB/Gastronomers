from django.shortcuts import render


# Create your views here.

def feed(request):
    return render(request, 'feed.html')


def comment(request):
    pass


def post(request):
    pass
