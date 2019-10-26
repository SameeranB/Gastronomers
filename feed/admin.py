from django.contrib import admin

# Register your models here.
from feed.models import Posts, Pictures, Comments

admin.site.register(Posts)
admin.site.register(Pictures)
admin.site.register(Comments)
