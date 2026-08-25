# Http404: excepción que Django convierte automáticamente en una
# respuesta HTTP 404 (página no encontrada).
from django.http import Http404
# render: combina un template con un contexto y devuelve el HttpResponse.
from django.shortcuts import render

# Create your views here.
# "Base de datos" en memoria de la tienda: un diccionario donde la clave
# es el slug de la categoría (el valor que aparece en la URL) y el valor
# es otro diccionario con el título a mostrar, el estilo del botón y los
# productos. "productos" es a su vez un diccionario cuya clave es el slug
# del producto (usado en la URL de detalle) y cuyo valor tiene nombre,
# imagen, precio y descripción.
CATEGORIAS = {
    "inciensos": {
        "titulo": "Inciensos",
        "icono": "🕯️",                  # Emoji que identifica la categoría en el botón.
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": {
            "incienso-suerte": {
                "nombre": "Incienso Suerte",
                "imagen": "images/item1.png",
                "precio": 900,
                "descripcion": "Aumenta la aparición de Pokémon durante 30 minutos. Ideal para cazar en zonas con poca actividad.",
            },
            "incienso-limpio": {
                "nombre": "Incienso Limpio",
                "imagen": "images/item2.png",
                "precio": 900,
                "descripcion": "Atrae Pokémon de tipo agua, planta y bicho con un aroma fresco y natural.",
            },
            "incienso-fulgor": {
                "nombre": "Incienso Fulgor",
                "imagen": "images/item3.png",
                "precio": 950,
                "descripcion": "Emite un brillo especial que atrae Pokémon raramente vistos en la zona.",
            },
        },
    },
    "pociones": {
        "titulo": "Pociones",
        "icono": "🧪",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": {
            "pocion": {
                "nombre": "Poción",
                "imagen": "images/item4.png",
                "precio": 300,
                "descripcion": "Restaura 20 PS de un Pokémon. La cura básica de todo entrenador.",
            },
            "superpocion": {
                "nombre": "Superpoción",
                "imagen": "images/item5.png",
                "precio": 500,
                "descripcion": "Restaura 50 PS de un Pokémon. Ideal para batallas más exigentes.",
            },
            "hiperpocion": {
                "nombre": "Hiperpoción",
                "imagen": "images/item6.png",
                "precio": 800,
                "descripcion": "Restaura 200 PS de un Pokémon. Recomendada antes de un gimnasio.",
            },
            "pocion-magica": {
                "nombre": "Poción Mágica",
                "imagen": "images/item7.png",
                "precio": 1200,
                "descripcion": "Restaura por completo los PS de un Pokémon al instante.",
            },
        },
    },
    "revivir": {
        "titulo": "Revivir",
        "icono": "✨",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": {
            "revivir": {
                "nombre": "Revivir",
                "imagen": "images/item8.png",
                "precio": 1500,
                "descripcion": "Revive a un Pokémon debilitado, devolviéndole la mitad de sus PS máximos.",
            },
            "revivir-maximo": {
                "nombre": "Revivir Máximo",
                "imagen": "images/item9.png",
                "precio": 2500,
                "descripcion": "Revive a un Pokémon debilitado, devolviéndole todos sus PS.",
            },
        },
    },
    "bayas": {
        "titulo": "Bayas",
        "icono": "🌿",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": {
            "baya-aranja": {
                "nombre": "Baya Aranja",
                "imagen": "images/item10.png",
                "precio": 200,
                "descripcion": "Cura por completo los PS de un Pokémon si se la das a comer.",
            },
            "baya-zidra": {
                "nombre": "Baya Zidra",
                "imagen": "images/item11.png",
                "precio": 250,
                "descripcion": "Facilita la captura de Pokémon dificiles de atrapar.",
            },
            "baya-meluce": {
                "nombre": "Baya Meluce",
                "imagen": "images/item12.png",
                "precio": 350,
                "descripcion": "Calma a un Pokémon salvaje y reduce sus posibilidades de huir.",
            },
        },
    },
    "monedas": {
        "titulo": "Monedas",
        "icono": "🪙",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": {
            "moneda-pokemon-go": {
                "nombre": "Moneda Pokémon GO",
                "imagen": "images/item14.png",
                "precio": 1,
                "descripcion": "Moneda individual utilizable en la tienda del juego.",
            },
            "moneda-x4": {
                "nombre": "Moneda X4",
                "imagen": "images/item17.png",
                "precio": 4,
                "descripcion": "Pack de 4 monedas para compras rápidas en la tienda.",
            },
            "moneda-x10": {
                "nombre": "Moneda x10",
                "imagen": "images/item19.png",
                "precio": 10,
                "descripcion": "Pack de 10 monedas, ideal para artículos de precio medio.",
            },
            "pack-s-monedas": {
                "nombre": "Pack S Monedas",
                "imagen": "images/item18.png",
                "precio": 550,
                "descripcion": "Pack pequeño de monedas a buen precio.",
            },
            "pack-m-monedas": {
                "nombre": "Pack M Monedas",
                "imagen": "images/item16.png",
                "precio": 1100,
                "descripcion": "Pack mediano de monedas, el más popular entre entrenadores.",
            },
            "pack-l-monedas": {
                "nombre": "Pack L Monedas",
                "imagen": "images/item15.png",
                "precio": 2200,
                "descripcion": "Pack grande de monedas para grandes compras en la tienda.",
            },
        },
    },
    "huevos_suerte": {
        "titulo": "Huevos suerte",
        "icono": "🥚",
        "color": "pokeball-black",     # Negro estilo Poké Ball.
        "productos": {
            "huevo-suerte": {
                "nombre": "Huevo Suerte",
                "imagen": "images/item23.png",
                "precio": 1000,
                "descripcion": "Duplica la experiencia obtenida durante 30 minutos.",
            },
            "huevo-suerte-pack-m": {
                "nombre": "Huevo Suerte Pack M",
                "imagen": "images/item21.png",
                "precio": 2800,
                "descripcion": "Pack de 3 Huevos Suerte para maximizar tu experiencia.",
            },
            "huevo-suerte-pack-l": {
                "nombre": "Huevo Suerte Pack L",
                "imagen": "images/item22.png",
                "precio": 4500,
                "descripcion": "Pack de 8 Huevos Suerte para entrenadores dedicados.",
            },
        },
    },
    "pokeballs": {
        "titulo": "Pokeballs",
        "icono": "⚪",
        "color": "pokeball-red",       # Rojo estilo Poké Ball.
        "productos": {
            "poke-ball": {
                "nombre": "Poké Ball",
                "imagen": "shopApp/images/pokeballs/poke-ball.png",
                "precio": 100,
                "descripcion": "La Poké Ball básica para capturar Pokémon.",
            },
            "super-ball": {
                "nombre": "Super Ball",
                "imagen": "shopApp/images/pokeballs/great-ball.png",
                "precio": 200,
                "descripcion": "Mejor tasa de captura que la Poké Ball estándar.",
            },
            "ultra-ball": {
                "nombre": "Ultra Ball",
                "imagen": "shopApp/images/pokeballs/ultra-ball.png",
                "precio": 400,
                "descripcion": "Alta tasa de captura, ideal para Pokémon fuertes.",
            },
            "master-ball": {
                "nombre": "Master Ball",
                "imagen": "shopApp/images/pokeballs/master-ball.png",
                "precio": 5000,
                "descripcion": "Captura garantizada al 100%. La Poké Ball definitiva.",
            },
            "safari-ball": {
                "nombre": "Safari Ball",
                "imagen": "shopApp/images/pokeballs/safari-ball.png",
                "precio": 300,
                "descripcion": "Solo funciona dentro de la Zona Safari.",
            },
            "net-ball": {
                "nombre": "Net Ball",
                "imagen": "shopApp/images/pokeballs/net-ball.png",
                "precio": 300,
                "descripcion": "Muy efectiva contra Pokémon tipo agua e insecto.",
            },
            "nest-ball": {
                "nombre": "Nest Ball",
                "imagen": "shopApp/images/pokeballs/nest-ball.png",
                "precio": 300,
                "descripcion": "Más efectiva cuanto más débil sea el nivel del Pokémon salvaje.",
            },
            "repeat-ball": {
                "nombre": "Repeat Ball",
                "imagen": "shopApp/images/pokeballs/repeat-ball.png",
                "precio": 300,
                "descripcion": "Muy efectiva contra especies ya registradas en la Pokédex.",
            },
            "timer-ball": {
                "nombre": "Timer Ball",
                "imagen": "shopApp/images/pokeballs/timer-ball.png",
                "precio": 300,
                "descripcion": "Su efectividad aumenta mientras más dure la batalla.",
            },
            "luxury-ball": {
                "nombre": "Luxury Ball",
                "imagen": "shopApp/images/pokeballs/luxury-ball.png",
                "precio": 300,
                "descripcion": "Acelera la relación de amistad con el Pokémon capturado.",
            },
            "premier-ball": {
                "nombre": "Premier Ball",
                "imagen": "shopApp/images/pokeballs/premier-ball.png",
                "precio": 100,
                "descripcion": "Poké Ball conmemorativa, funciona igual que la estándar.",
            },
            "dive-ball": {
                "nombre": "Dive Ball",
                "imagen": "shopApp/images/pokeballs/dive-ball.png",
                "precio": 300,
                "descripcion": "Muy efectiva contra Pokémon que viven bajo el agua.",
            },
            "dusk-ball": {
                "nombre": "Dusk Ball",
                "imagen": "shopApp/images/pokeballs/dusk-ball.png",
                "precio": 300,
                "descripcion": "Muy efectiva de noche o en cuevas oscuras.",
            },
            "heal-ball": {
                "nombre": "Heal Ball",
                "imagen": "shopApp/images/pokeballs/heal-ball.png",
                "precio": 300,
                "descripcion": "Cura por completo al Pokémon capturado al usarla.",
            },
            "quick-ball": {
                "nombre": "Quick Ball",
                "imagen": "shopApp/images/pokeballs/quick-ball.png",
                "precio": 300,
                "descripcion": "Muy efectiva si se usa en el primer turno de la batalla.",
            },
            "cherish-ball": {
                "nombre": "Cherish Ball",
                "imagen": "shopApp/images/pokeballs/cherish-ball.png",
                "precio": 500,
                "descripcion": "Poké Ball especial reservada para eventos y Pokémon distribuidos.",
            },
        },
    },
}


# Vista de inicio de la tienda: muestra los botones de cada categoría.
def home(request):
    # Se pasa todo el diccionario CATEGORIAS al template para poder
    # iterarlo como pares (slug, data) sin chocar con claves como "items".
    return render(request, 'shopApp/home.html', {"categorias": list(CATEGORIAS.items())})


# Vista de detalle de categoría. "nombre" llega desde la URL gracias a
# <str:nombre> definido en shopApp/urls.py (ej: /pokeballs/).
def categoria(request, nombre):
    # .get() devuelve None si la clave no existe, en vez de lanzar KeyError.
    data = CATEGORIAS.get(nombre)
    if data is None:
        # Si la categoría no existe (URL inventada), respondemos con un 404.
        raise Http404("Categoría no encontrada")
    # "productos" ahora es un diccionario {slug: producto}. Lo convertimos
    # a lista de pares (slug, producto) para poder iterarlo en el template
    # y armar el link de detalle con el slug de cada producto.
    context = {
        "slug": nombre,
        "titulo": data["titulo"],
        "color": data["color"],
        "productos": list(data["productos"].items()),
    }
    return render(request, 'shopApp/categoria.html', context)


# Vista de detalle de un producto individual.
# "categoria" y "producto" llegan desde la URL (ej: /pokeballs/master-ball/).
def detalle_producto(request, categoria, producto):
    data = CATEGORIAS.get(categoria)
    if data is None:
        raise Http404("Categoría no encontrada")
    # Busca el producto dentro del diccionario "productos" de esa categoría.
    info_producto = data["productos"].get(producto)
    if info_producto is None:
        raise Http404("Producto no encontrado")
    context = {
        "categoria_slug": categoria,
        "categoria_titulo": data["titulo"],
        **info_producto,  # nombre, imagen, precio, descripcion
    }
    return render(request, 'shopApp/detalle.html', context)
