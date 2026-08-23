# path: función para declarar una ruta URL.
from django.urls import path
# Vistas de esta app que vamos a mapear a rutas.
from shopApp.views import home, categoria

# Rutas propias de shopApp. Como en pokeMarketProject/urls.py se incluyó con
# path('', include('shopApp.urls')), estas rutas quedan montadas en la raíz del sitio.
urlpatterns = [
    # '' (raíz del sitio, ej: /) -> vista home.
    path('', home, name='shop_home'),
    # '<str:nombre>/' captura cualquier texto en la URL y lo pasa como
    # el argumento "nombre" a la vista categoria.
    # Ejemplo: /electronica/ -> categoria(request, nombre="electronica")
    path('<str:nombre>/', categoria, name='shop_categoria'),
]
