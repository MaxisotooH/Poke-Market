# Poke Market

Proyecto Django que simula una tienda en línea con página principal y 3 categorías de productos (Electrónica, Juguetes, Ropa).

## Requisitos

- Python 3.10+
- Django 5.2

## Instalación

```bash
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

## Correr el servidor

```bash
python manage.py migrate
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

## Rutas

| URL | Descripción |
|---|---|
| `/` | Página principal con las categorías |
| `/electronica/` | Categoría Electrónica |
| `/juguetes/` | Categoría Juguetes |
| `/ropa/` | Categoría Ropa |
| `/admin/` | Panel de administración |

## Estructura

```
pokeMarket/
├── manage.py
├── pokeMarketProject/   # Configuración del proyecto (settings, urls)
├── shopApp/              # App con las vistas de la tienda
├── templates/shopApp/    # Templates HTML
└── static/shopApp/       # CSS y logo
```
