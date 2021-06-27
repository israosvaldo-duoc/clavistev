from django.urls import path
from .views import home, crear_celular, listado_celulares, eliminar_celulares, editar_celulares

urlpatterns = [
    path('', home, name="home"),
    path('crear-celular/', crear_celular, name="crear_celular"),
    path('listado-celulares/', listado_celulares, name="listado_celulares"),
    path('eliminar-celulares/<int:pk>',eliminar_celulares, name="eliminar_celulares"),
    path('editar-celulares/<int:id>', editar_celulares, name="editar_celulares"),
]