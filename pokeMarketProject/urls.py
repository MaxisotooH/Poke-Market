"""
URL configuration for pokeMarketProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
# admin: panel de administración incluido por defecto en Django.
from django.contrib import admin
# path: define una ruta URL individual.
# include: delega un prefijo de URL a otro archivo urls.py (el de la app).
from django.urls import include, path

from .views import index

# Lista de rutas del proyecto.
urlpatterns = [
    # /admin/ -> panel de administración de Django.
    path('admin/', admin.site.urls),
    # '' -> index.html, la página de inicio real del sitio. Enlaza a las
    # apps productos y usuarios (ver templates/index.html y shop_base.html).
    path('', index, name='index'),
    # /usuarios/... -> registro, login, logout y perfil, definidas en
    # usuarios/urls.py.
    path('usuarios/', include('usuarios.urls')),
    # /productos/... -> catálogo de la tienda (shopApp): home con
    # categorías, detalle de categoría y detalle de producto.
    path('productos/', include('shopApp.urls')),
]
