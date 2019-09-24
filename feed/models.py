from django.db import models

# Create your models here.
from main.models import Restaurant, Dish
from user.models import CustomUser


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    rating = models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])
    shares = models.IntegerField()
    caption = models.TextField()


class Pictures(models.Model):
    picture_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    picture = models.ImageField()


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.TextField()
