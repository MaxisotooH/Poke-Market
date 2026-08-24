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
        "productos": [
            {"nombre": "Incienso Suerte", "imagen": "images/item1.png"},
            {"nombre": "Incienso Limpio", "imagen": "images/item2.png"},
            {"nombre": "Incienso Fulgor", "imagen": "images/item3.png"},
        ],
    },
    "pociones": {
        "titulo": "Pociones",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": [
            {"nombre": "Poción", "imagen": "images/item4.png"},
            {"nombre": "Superpoción", "imagen": "images/item5.png"},
            {"nombre": "Hiperpoción", "imagen": "images/item6.png"},
            {"nombre": "Poción Mágica", "imagen": "images/item7.png"},
        ],
    },
    "revivir": {
        "titulo": "Revivir",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": [
            {"nombre": "Revivir", "imagen": "images/item8.png"},
            {"nombre": "Revivir Máximo", "imagen": "images/item9.png"},
        ],
    },
    "bayas": {
        "titulo": "Bayas",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": [
            {"nombre": "Baya Aranja", "imagen": "images/item10.png"},
            {"nombre": "Baya Zidra", "imagen": "images/item11.png"},
            {"nombre": "Baya Meluce", "imagen": "images/item12.png"},
        ],
    },
    "monedas": {
        "titulo": "Monedas",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": [
            {"nombre": "Moneda Pokémon GO", "imagen": "images/item14.png"},
            {"nombre": "Moneda X4", "imagen": "images/item17.png"},
            {"nombre": "Moneda x10", "imagen": "images/item19.png"},
            {"nombre": "Pack S Monedas", "imagen": "images/item18.png"},
            {"nombre": "Pack M Monedas", "imagen": "images/item16.png"},
            {"nombre": "Pack L Monedas", "imagen": "images/item15.png"},
        ],
    },
    "huevos_suerte": {
        "titulo": "Huevos suerte",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": [
            {"nombre": "Huevo Suerte", "imagen": "images/item23.png"},
            {"nombre": "Huevo Suerte Pack M", "imagen": "images/item21.png"},
            {"nombre": "Huevo Suerte Pack L", "imagen": "images/item22.png"},
            
        ],
    },
    "pokeballs": {
        "titulo": "Pokeballs",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": [
            {"nombre": "Poké Ball", "imagen": "shopApp/images/pokeballs/poke-ball.png"},
            {"nombre": "Super Ball", "imagen": "shopApp/images/pokeballs/great-ball.png"},
            {"nombre": "Ultra Ball", "imagen": "shopApp/images/pokeballs/ultra-ball.png"},
            {"nombre": "Master Ball", "imagen": "shopApp/images/pokeballs/master-ball.png"},
            {"nombre": "Safari Ball", "imagen": "shopApp/images/pokeballs/safari-ball.png"},
            {"nombre": "Net Ball", "imagen": "shopApp/images/pokeballs/net-ball.png"},
            {"nombre": "Nest Ball", "imagen": "shopApp/images/pokeballs/nest-ball.png"},
            {"nombre": "Repeat Ball", "imagen": "shopApp/images/pokeballs/repeat-ball.png"},
            {"nombre": "Timer Ball", "imagen": "shopApp/images/pokeballs/timer-ball.png"},
            {"nombre": "Luxury Ball", "imagen": "shopApp/images/pokeballs/luxury-ball.png"},
            {"nombre": "Premier Ball", "imagen": "shopApp/images/pokeballs/premier-ball.png"},
            {"nombre": "Dive Ball", "imagen": "shopApp/images/pokeballs/dive-ball.png"},
            {"nombre": "Dusk Ball", "imagen": "shopApp/images/pokeballs/dusk-ball.png"},
            {"nombre": "Heal Ball", "imagen": "shopApp/images/pokeballs/heal-ball.png"},
            {"nombre": "Quick Ball", "imagen": "shopApp/images/pokeballs/quick-ball.png"},
            {"nombre": "Cherish Ball", "imagen": "shopApp/images/pokeballs/cherish-ball.png"},
        ],
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
