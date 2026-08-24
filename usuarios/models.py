from django.db import models
# User: modelo de usuario incluido por defecto en Django (username, password,
# email, etc). Lo extendemos con datos propios de un "entrenador" en vez de
# modificarlo directamente, usando una relación uno a uno.
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    """Datos adicionales de un cliente de la tienda, ligados 1 a 1 con
    el User de autenticación de Django."""

    # OneToOneField: cada User tiene como máximo un Perfil y viceversa.
    # related_name='perfil' permite acceder a esto como user.perfil.
    # on_delete=CASCADE: si se borra el User, se borra también su Perfil.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    # Apodo de entrenador Pokémon, propio de la temática de la tienda.
    apodo_entrenador = models.CharField(max_length=50, blank=True)
    # Región Pokémon favorita, dato simple de perfil pedido en el registro.
    region_favorita = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
