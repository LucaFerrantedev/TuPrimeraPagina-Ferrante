from django.contrib import admin
from django.urls import path
from productos.views import home, componentes_list, agregar_marca, agregar_categoria, agregar_componente

urlpatterns = [
   #path('admin/', admin.site.urls),
   path("", home, name="home"),
   path("productos/", componentes_list, name="productos_list"),
   path("productos/crear_marca/", agregar_marca, name="marca_create"),
   path("productos/crear_categoria/", agregar_categoria, name="categoria_create"),
   path("productos/crear_componente/", agregar_componente, name="componente_create")
]
