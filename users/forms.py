from django import forms
from .models import User


class UserRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name', 'surname', 'bio', 'subject', 'avatar,', 'gender']


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'bio', 'subject', 'avatar', 'gender']
