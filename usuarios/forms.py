from django import forms
# UserCreationForm: formulario base de Django para crear un User
# (username + password + confirmación), con validaciones de seguridad
# de contraseña ya incluidas.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    """Extiende el formulario de registro de Django agregando el email
    y los datos propios del perfil de entrenador (apodo, región).
    email, apodo_entrenador y region_favorita no existen en el User
    estándar de Django, así que se declaran como campos extra del
    formulario y se guardan a mano en la vista de registro."""

    email = forms.EmailField(required=True)
    apodo_entrenador = forms.CharField(max_length=50, required=False, label="Apodo de entrenador")
    region_favorita = forms.CharField(max_length=50, required=False, label="Región favorita")

    class Meta(UserCreationForm.Meta):
        model = User
        # Campos que se piden en el formulario, además de password1/password2
        # que UserCreationForm ya agrega automáticamente.
        fields = ["username", "email"]
