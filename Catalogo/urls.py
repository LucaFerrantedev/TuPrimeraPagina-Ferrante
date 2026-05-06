from django.contrib import admin
from django.urls import path
from productos.views import CategoriaCreateView, ComponenteCreateView, ComponentesListView, MarcaCreateView, home
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
   #path('admin/', admin.site.urls),
   path("", home, name="home"),
   path("productos/", ComponentesListView.as_view(), name="productos_list"),
   path("productos/crear_marca/", MarcaCreateView.as_view(), name="marca_create"),
   path("productos/crear_categoria/", CategoriaCreateView.as_view(), name="categoria_create"),
   path("productos/crear_componente/", ComponenteCreateView.as_view(), name="componente_create"),
   path('cambiar_password/', PasswordChangeView.as_view(
        template_name='accounts/cambiar_password.html',
        success_url='/' # A dónde ir después de cambiarla con éxito
    ), name='cambiar_password'),
]
