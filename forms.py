from django import forms
from django.contrib.auth.models import User

from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_log']




class UserForm(forms.ModelForm):
    #widget=forms.PasswordInput: hide the input charactor
    password = forms.CharField(widget=forms.PasswordInput)

    #class meta: information of the class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
