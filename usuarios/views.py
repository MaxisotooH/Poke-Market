# login: inicia sesión al usuario recién registrado automáticamente,
# para que no tenga que loguearse a mano después de registrarse.
# login_required: decorador que protege una vista, redirigiendo a
# LOGIN_URL (settings.py) si el usuario no está autenticado.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegistroForm
from .models import Perfil


# Create your views here.
def registro(request):
    if request.method == "POST":
        # Reconstruye el formulario con los datos enviados para validarlos.
        form = RegistroForm(request.POST)
        if form.is_valid():
            # form.save() crea y guarda el User (username, email, password).
            usuario = form.save()
            # Crea el Perfil asociado con los datos extra del formulario,
            # que no forman parte del modelo User estándar.
            Perfil.objects.create(
                user=usuario,
                apodo_entrenador=form.cleaned_data.get("apodo_entrenador", ""),
                region_favorita=form.cleaned_data.get("region_favorita", ""),
            )
            # Inicia sesión automáticamente con el usuario recién creado.
            login(request, usuario)
            return redirect("usuarios_perfil")
    else:
        # GET: formulario vacío, primera vez que se visita la página.
        form = RegistroForm()
    return render(request, "usuarios/registro.html", {"form": form})


# @login_required: si no hay sesión iniciada, redirige a LOGIN_URL
# (definido en settings.py) en vez de ejecutar la vista.
@login_required
def perfil(request):
    # get_or_create evita un error si un usuario antiguo (creado antes de
    # que existiera el modelo Perfil) todavía no tiene uno asociado.
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, "usuarios/perfil.html", {"perfil": perfil_usuario})
