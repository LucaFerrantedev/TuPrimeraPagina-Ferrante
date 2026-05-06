from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Account


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("username", "email")


class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "telefono", "avatar")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }