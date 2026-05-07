from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from productos.models import MarcaProductos,CategoriaProductos, ComponenteProductos
from productos.forms import MarcaProductosForm, CategoriaProductosForm, ComponenteProductosForm


def home(request):
    return render(request, "productos/index.html")

class MarcaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MarcaProductos
    form_class = MarcaProductosForm
    template_name = "productos/marca_create.html"
    success_url = reverse_lazy("productos_list")

    def test_func(self):
        return self.request.user.is_superuser

class CategoriaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CategoriaProductos
    form_class = CategoriaProductosForm
    template_name = "productos/categoria_create.html"
    success_url = reverse_lazy("productos_list")

    def test_func(self):
        return self.request.user.is_superuser

class ComponenteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ComponenteProductos
    form_class = ComponenteProductosForm
    template_name = "productos/componente_create.html"
    success_url = reverse_lazy("productos_list")

    def test_func(self):
        return self.request.user.is_superuser

class ComponentesListView(ListView):
    model = ComponenteProductos
    template_name = "productos/productos_list.html"
    context_object_name = "productos_list"

    def get_queryset(self):
        query_list = super().get_queryset()
        query = self.request.GET.get("nombre") 
        
        if query:
            query_list = query_list.filter(modelo__icontains=query)
            
        return query_list

class ComponenteDetailView(DetailView):
    model = ComponenteProductos
    template_name = "productos/producto_detail.html"
    context_object_name = "producto"
    slug_field = "sku"
    slug_url_kwarg = "sku"

class ComponenteUpdateView(LoginRequiredMixin, UpdateView):
    model = ComponenteProductos
    #fields = ("imagen", "modelo", "precio", "descripcion", "marca", "categoria", "sku")
    form_class = ComponenteProductosForm
    template_name = "productos/componente_update.html"
    slug_field = "sku"
    slug_url_kwarg = "sku"

    def get_success_url(self):
        return reverse_lazy(
            "producto_detail",
            kwargs={"sku": self.object.sku}
        )
    
    def test_func(self):
        return self.request.user.is_superuser

class ComponenteDeleteView(LoginRequiredMixin, DeleteView):
    model = ComponenteProductos
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("productos_list")
    slug_field = "sku"
    slug_url_kwarg = "sku"

    def test_func(self):
        return self.request.user.is_superuser

def about(request):
    return render(request, "productos/about.html")