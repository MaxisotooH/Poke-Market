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

# Lista de rutas del proyecto. Como POKE MARKET es la única app,
# se monta directamente en la raíz del sitio ('').
urlpatterns = [
    # /admin/ -> panel de administración de Django.
    path('admin/', admin.site.urls),
    # '' -> todas las rutas de la tienda, definidas en shopApp/urls.py
    # (home en '/', categorías en '/<nombre>/').
    path('', include('shopApp.urls')),
]
