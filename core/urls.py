from django.urls import path

from .views import home, crear_celular, listado_celulares

urlpatterns = [
    path('', home, name="home"),
    path('crear-celular/', crear_celular, name="crear_celular"),
    path('listado-celulares/', listado_celulares, name="listado_celulares")

]