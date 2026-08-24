from django.shortcuts import render


# index: página de inicio real del sitio (ruta '/'). No pertenece a
# shopApp ni a usuarios porque es el punto de entrada que enlaza a ambas
# apps, así que vive directamente en el proyecto.
def index(request):
    return render(request, 'index.html')
