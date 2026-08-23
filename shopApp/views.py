# Http404: excepción que Django convierte automáticamente en una
# respuesta HTTP 404 (página no encontrada).
from django.http import Http404
# render: combina un template con un contexto y devuelve el HttpResponse.
from django.shortcuts import render

# Create your views here.
# "Base de datos" en memoria de la tienda: un diccionario donde la clave
# es el slug de la categoría (el valor que aparece en la URL) y el valor
# es otro diccionario con el título a mostrar, el estilo del botón y la
# lista de productos.
CATEGORIAS = {
    "inciensos": {
        "titulo": "Inciensos",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": ["Incienso Suerte", "Incienso Limpio", "Incienso Fulgor"],
    },
    "pociones": {
        "titulo": "Pociones",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": ["Poción", "Superpoción", "Hiperpoción"],
    },
    "revivir": {
        "titulo": "Revivir",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": ["Revivir", "Revivir Máximo", "Revivir Total"],
    },
    "bayas": {
        "titulo": "Bayas",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": ["Baya Aranja", "Baya Zidra", "Baya Meluce"],
    },
    "monedas": {
        "titulo": "Monedas",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": ["Moneda Amuleto", "Moneda Rápida", "Monedas de Liga"],
    },
    "huevos_suerte": {
        "titulo": "Huevos suerte",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": ["Huevo Suerte", "Huevo Suerte XL", "Huevo Suerte Premium"],
    },
    "pokeballs": {
        "titulo": "Pokeballs",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": ["Poké Ball", "Super Ball", "Ultra Ball"],
    },
}


# Vista de inicio de la tienda: muestra los botones de cada categoría.
def home(request):
    # Se pasa todo el diccionario CATEGORIAS al template para poder
    # iterarlo como pares (slug, data) sin chocar con claves como "items".
    return render(request, 'shopApp/home.html', {"categorias": list(CATEGORIAS.items())})


# Vista de detalle de categoría. "nombre" llega desde la URL gracias a
# <str:nombre> definido en shopApp/urls.py (ej: /electronica/).
def categoria(request, nombre):
    # .get() devuelve None si la clave no existe, en vez de lanzar KeyError.
    data = CATEGORIAS.get(nombre)
    if data is None:
        # Si la categoría no existe (URL inventada), respondemos con un 404.
        raise Http404("Categoría no encontrada")
    # "slug": nombre se agrega para poder mostrarlo si se necesita en el template.
    # **data "desempaqueta" el diccionario (titulo, color, productos) como
    # claves sueltas del contexto final.
    return render(request, 'shopApp/categoria.html', {"slug": nombre, **data})
