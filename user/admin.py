from django.contrib import admin

# Register your models here.
from user.models import CustomUser, Follows

admin.site.register(CustomUser)
admin.site.register(Follows)