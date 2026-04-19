from django import forms
from productos.models import MarcaProductos, CategoriaProductos, ComponenteProductos

class MarcaProductosForm(forms.ModelForm):
    class Meta:
        model = MarcaProductos
        fields = ("nombre",)
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'})
        }

class CategoriaProductosForm(forms.ModelForm):
    class Meta:
        model = CategoriaProductos
        fields = ("tipo_prod",)
        widgets = {
            "tipo_prod": forms.TextInput(attrs={'class': 'form-control'})
        }

class ComponenteProductosForm(forms.ModelForm):
    class Meta:
        model = ComponenteProductos
        fields = ("modelo", "precio", "descripcion", "marca", "categoria")
        widgets = {
            "modelo": forms.TextInput(attrs={'class': 'form-control'}),
            "precio": forms.DecimalField(attrs={'class': 'form-control'}),
            "descripcion": forms.TextInput(attrs={'class': 'form-control'}),
            "marca": forms.TextInput(attrs={'class': 'form-control'}),
            "marca": forms.TextInput(attrs={'class': 'form-control'})
        }
