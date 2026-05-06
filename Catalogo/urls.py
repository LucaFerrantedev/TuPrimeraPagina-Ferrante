from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from productos.views import (CategoriaCreateView, ComponenteCreateView, ComponentesListView, 
                             ComponenteDetailView, ComponenteUpdateView, ComponenteDeleteView,
                             MarcaCreateView, home, about)
from accounts.views import register, account_detail, account_change

urlpatterns = [
   path('admin/', admin.site.urls), # ¡Descomentado para que puedas entrar al panel!
   path("", home, name="home"),
   path("about/", about, name="about"), # Ruta del Acerca de mí
   
   path("productos/", ComponentesListView.as_view(), name="productos_list"),
   path("productos/crear_marca/", MarcaCreateView.as_view(), name="marca_create"),
   path("productos/crear_categoria/", CategoriaCreateView.as_view(), name="categoria_create"),
   path("productos/crear_componente/", ComponenteCreateView.as_view(), name="componente_create"),

   path("productos/<int:sku>/", ComponenteDetailView.as_view(), name="producto_detail"),
   path("productos/<int:sku>/editar/", ComponenteUpdateView.as_view(), name="componente_update"),
   path("productos/<int:sku>/borrar/", ComponenteDeleteView.as_view(), name="componente_delete"),

   path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('registro/', register, name='register'),
   path('cuenta/', account_detail, name='account_detail'),
   path('cuenta/editar/', account_change, name='account_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    