from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadFileForm(forms.Form):
    class Meta:
        file = forms.FileField()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            fields[1]: forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
