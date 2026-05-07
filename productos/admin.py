from django.contrib import admin
from .models import MarcaProductos, CategoriaProductos, ComponenteProductos

admin.site.register(MarcaProductos)
admin.site.register(CategoriaProductos)
admin.site.register(ComponenteProductos)