# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ("username", "email", "state")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ("username", "email")