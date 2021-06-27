from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def eliminar_celulares(request):
    return render(request, 'core/eliminar_celulares.html')    