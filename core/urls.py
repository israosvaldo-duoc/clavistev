from django.urls import path
from .views import home, listado_celulares

urlpatterns = [
    path('', home, name="home"),
    path('listado-celulares/', listado_celulares, name="listado_celulares")
]