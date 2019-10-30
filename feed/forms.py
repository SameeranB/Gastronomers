from django import forms

from feed.models import Posts
from main.models import Restaurant


class PostForm(forms.ModelForm):
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all())

    class Meta:
        model = Posts
        fields = ('restaurant', 'pic', 'caption')
