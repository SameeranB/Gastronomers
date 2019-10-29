from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True, null=True)
    thumbnail = models.ImageField(null=True)
