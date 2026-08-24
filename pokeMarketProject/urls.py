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

# Lista de rutas del proyecto.
urlpatterns = [
    # /admin/ -> panel de administración de Django.
    path('admin/', admin.site.urls),
    # /usuarios/... -> registro, login, logout y perfil, definidas en
    # usuarios/urls.py. DEBE ir antes que shopApp: shopApp monta una ruta
    # catch-all de 2 segmentos ('<categoria>/<producto>/') en la raíz, y si
    # esta línea fuera después, "usuarios/registro/" sería interpretado
    # como categoria="usuarios", producto="registro" por la tienda.
    path('usuarios/', include('usuarios.urls')),
    # '' -> todas las rutas de la tienda, definidas en shopApp/urls.py
    # (home en '/', categorías en '/<nombre>/', detalle en '/<cat>/<prod>/').
    path('', include('shopApp.urls')),
]
