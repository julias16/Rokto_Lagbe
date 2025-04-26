from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


