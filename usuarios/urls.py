from django.urls import path
# auth_views: vistas de login/logout ya implementadas por Django, solo
# hace falta indicarles qué template usar y a dónde redirigir.
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # /usuarios/registro/ -> formulario de registro (crea User + Perfil).
    path("registro/", views.registro, name="usuarios_registro"),
    # /usuarios/login/ -> LoginView built-in de Django, usando nuestro template.
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="usuarios/login.html"),
        name="usuarios_login",
    ),
    # /usuarios/logout/ -> cierra la sesión y redirige a LOGOUT_REDIRECT_URL
    # (definido en settings.py como 'shop_home').
    path("logout/", auth_views.LogoutView.as_view(), name="usuarios_logout"),
    # /usuarios/perfil/ -> vista protegida con @login_required.
    path("perfil/", views.perfil, name="usuarios_perfil"),
]
