from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Account


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("username", "email")

        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
            "email": forms.EmailInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control bg-dark text-white border-secondary'


class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "dni", "telefono", "direccion", "pais", "avatar")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }