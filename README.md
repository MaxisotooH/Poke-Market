# Poké Market

Aplicación web en Django que simula una tienda en línea temática Pokémon. Cuenta con una página de inicio, un catálogo de productos organizado por categorías con vista de detalle (imagen, descripción y precio), y un sistema de cuentas de usuario (registro, login, perfil de entrenador).

## Tecnologías utilizadas

- **Python 3.10+**
- **Django 5.2** — framework web principal
- **django-crispy-forms 2.7** + **crispy-bootstrap5** — renderizado de formularios (registro/login) con estilos de Bootstrap
- **Bootstrap 5.3.3** (vía CDN) — utilidades base de layout y componentes
- **SQLite** — base de datos de desarrollo (`db.sqlite3`, generada localmente, no se versiona)
- **HTML5 / CSS3** — templates y estilos propios con temática "Poké Ball" (`static/shopApp/shop.css`)
- **Google Fonts** (Bangers, Luckiest Guy) — tipografías del sitio

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
git clone https://github.com/MaxisotooH/Poke-Market.git
cd Poke-Market

python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

## Configuración inicial de la base de datos

La primera vez (y cada vez que `db.sqlite3` no exista o esté vacío):

```bash
python manage.py migrate
```

Opcional, para acceder al panel de administración (`/admin/`):

```bash
python manage.py createsuperuser
```

## Correr el servidor

```bash
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

## Estructura del proyecto

```
Poke-Market/
├── manage.py
├── requirements.txt
├── db.sqlite3                  # Generado localmente por migrate (no se versiona)
├── pokeMarketProject/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py                 # Rutas raíz: index, /usuarios/, /productos/
│   └── views.py                # Vista index (página de inicio)
├── shopApp/                    # App "productos": catálogo, categorías, detalle
│   ├── views.py                # home, categoria, detalle_producto
│   ├── urls.py
│   └── models.py
├── usuarios/                   # App "usuarios": registro, login, perfil
│   ├── models.py               # Perfil (1 a 1 con User: apodo, región favorita)
│   ├── forms.py                # RegistroForm (extiende UserCreationForm)
│   ├── views.py                # registro, perfil (login_required)
│   └── urls.py
├── templates/
│   ├── index.html
│   ├── shopApp/                # shop_base.html, home.html, categoria.html, detalle.html
│   └── usuarios/                # registro.html, login.html, perfil.html
└── static/
    ├── images/                 # Imágenes de productos
    └── shopApp/                # shop.css, logo, imágenes de pokeballs
```

## Apps

### `shopApp` (productos)

Gestiona el catálogo: categorías (inciensos, pociones, revivir, bayas, monedas, huevos suerte, pokeballs) y sus productos, cada uno con nombre, imagen, precio y descripción organizados en diccionarios de Python dentro de `views.py`.

### `usuarios`

Gestiona cuentas de cliente sobre el sistema de autenticación de Django (`User`), extendido con un modelo `Perfil` (apodo de entrenador, región favorita). Incluye registro (con login automático), inicio/cierre de sesión y una vista de perfil protegida.

## Rutas

| URL | Descripción |
|---|---|
| `/` | Página de inicio, con menú de navegación a Productos y Usuarios |
| `/productos/` | Catálogo: lista de categorías |
| `/productos/<categoria>/` | Productos de una categoría |
| `/productos/<categoria>/<producto>/` | Detalle de un producto (imagen, descripción, precio) |
| `/usuarios/registro/` | Crear cuenta de entrenador |
| `/usuarios/login/` | Iniciar sesión |
| `/usuarios/logout/` | Cerrar sesión |
| `/usuarios/perfil/` | Perfil del usuario autenticado (requiere sesión) |
| `/admin/` | Panel de administración de Django |
