from django.urls import path, include, re_path
from .views import *

app_name = "Feed"

urlpatterns = [
    path('feed', feed, name="Feed"),
    path('comment', comment, name="Comment"),
    path('post-comment', post, name="Post")
]