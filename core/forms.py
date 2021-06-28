from django.contrib.auth.forms import UserCreationForm
from django import forms
from core.models import User, ToDo


class LoginForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class TodoCreationForm(forms.ModelForm):
    user = forms.Field(required=False)

    class Meta:
        model = ToDo
        fields = [
            'text',
            'user',
        ]