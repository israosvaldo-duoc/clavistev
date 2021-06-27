from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def listado_celulares(request):
    return render(request, 'core/listado_celulares.html')

def crear_celular(request):
    return render(request, 'core/crear_celular.html')

def eliminar_celulares(request):
    return render(request, 'core/eliminar_celulares.html') 


