from django.db import models

# Create your models here.
from main.models import Restaurant, Dish
from user.models import CustomUser


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.IntegerField(default=0)
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True, null=True)
    shares = models.IntegerField(default=0, blank=True, null=True)
    caption = models.TextField()
    posted_date = models.DateTimeField(auto_now=True)
    pic = models.ImageField(blank=True, null=True, upload_to='media')


class Pictures(models.Model):
    picture_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    picture = models.ImageField()


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
