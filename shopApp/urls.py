# path: función para declarar una ruta URL.
from django.urls import path
# Vistas de esta app que vamos a mapear a rutas.
from shopApp.views import home, categoria, detalle_producto

# Rutas propias de shopApp. Como en pokeMarketProject/urls.py se incluyó con
# path('', include('shopApp.urls')), estas rutas quedan montadas en la raíz del sitio.
urlpatterns = [
    # '' (raíz del sitio, ej: /) -> vista home.
    path('', home, name='shop_home'),
    # '<str:categoria>/<str:producto>/' captura categoría y producto como
    # dos segmentos de la URL (ej: /pokeballs/master-ball/) y los pasa a
    # detalle_producto. Se declara ANTES que la ruta de categoría de un
    # solo segmento para que Django la reconozca correctamente.
    path('<str:categoria>/<str:producto>/', detalle_producto, name='shop_detalle'),
    # '<str:nombre>/' captura cualquier texto en la URL y lo pasa como
    # el argumento "nombre" a la vista categoria.
    # Ejemplo: /pokeballs/ -> categoria(request, nombre="pokeballs")
    path('<str:nombre>/', categoria, name='shop_categoria'),
]
