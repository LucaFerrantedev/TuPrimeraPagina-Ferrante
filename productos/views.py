from django.shortcuts import render, get_object_or_404, redirect
from productos.models import MarcaProductos
from productos.models import CategoriaProductos
from productos.models import ComponenteProductos
from productos.forms import MarcaProductosForm
from productos.forms import CategoriaProductosForm
from productos.forms import ComponenteProductosForm
from django.http import Http404

def home(request):
    return render(request, "productos/index.html")

def agregar_marca(request):
    if request.method == "POST":
        form = MarcaProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos_list")
    else:
        form = MarcaProductosForm()

    return render(request, "productos/marca_create.html", {"form": form})

def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos_list")
    else:
        form = CategoriaProductosForm()

    return render(request, "productos/categoria_create.html", {"form": form})

def agregar_componente(request):
    if request.method == "POST":
        form = ComponenteProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos_list")
    else:
        form = ComponenteProductosForm()

    return render(request, "productos/componente_create.html", {"form": form})

def componentes_list(request):
    modelo = request.GET.get("nombre")
    componentes_query = ComponenteProductos.objects.all()
    if modelo is not None:
        componentes_query = ComponenteProductos.objects.filter(
            modelo__icontains=modelo
        )
    contexto = {
        "componentes_list": list(componentes_query)
    }

    return render(request, "productos/productos_list.html", contexto)