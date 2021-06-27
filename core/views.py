from core.models import Celular
from django.shortcuts import render
from .models import Celular

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def listado_celulares(request):
    # Creamos una variable que traiga el listado de celulares desde la BD
    celulares = Celular.objects.all()
    # Creamos un objeto data que traspasará los datos para utilizarlos en el html asociado
    data = {
        'celulares': celulares
    }
    # Traspasamos data como tercer parámetro al momento de randerizar 
    return render(request, 'core/listado_celulares.html', data)

def crear_celular(request):
    return render(request, 'core/crear_celular.html')

def editar_celulares(request):
    return render(request, 'core/editar_celulares.html')

def eliminar_celulares(request):
    return render(request, 'core/eliminar_celulares.html') 


