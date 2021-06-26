from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def listado_celulares(request):
    return render(request, 'core/listado_celulares.html')