from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    organization = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'organization', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
