from django.db import models


# Create your models here.

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    location = models.TextField(unique=True)
    logo = models.ImageField(null=True, blank=True)
    pintrest = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    establishment_year = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)
    overview = models.TextField(default="")

    def __str__(self):
        return self.name


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
