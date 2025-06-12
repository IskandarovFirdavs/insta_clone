from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserRegister(UserCreationForm):
    name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['name', 'surname']


class UserLogin(AuthenticationForm):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)


class UserUpdate(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    bio = forms.CharField(max_length=250, required=True)
    avatar = forms.FileField(upload_to='user/avatar')
    email = forms.EmailField(unique=True, required=True)
    gender = forms.CharField(max_length=10,)
    subject = forms.CharField(max_length=10, required=True)

class Meta:
    model = User
    fields = ['name', 'surname', 'username', 'bio', 'avatar', 'email', 'gender', 'subject']


