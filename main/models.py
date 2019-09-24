from django.db import models


# Create your models here.

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    location = models.TextField(unique=True)


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    description = models.TextField()
    price = models.IntegerField()

