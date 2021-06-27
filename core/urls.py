from django.urls import path
from .views import home, eliminar_celulares

urlpatterns = [
    path('', home, name="home"),
    path('eliminar-celulares/',eliminar_celulares, name="eliminar_celulares"),
]