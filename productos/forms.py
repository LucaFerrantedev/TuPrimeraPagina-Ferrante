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
        fields = ("imagen", "modelo", "sku", "precio", "descripcion", "marca", "categoria")
        widgets = {
            "imagen": forms.ClearableFileInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
            "modelo": forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
            "sku": forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
            "precio": forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
            "descripcion": forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
            "marca": forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            "categoria": forms.Select(attrs={'class': 'form-select bg-dark text-white border-secondary'})
        }
