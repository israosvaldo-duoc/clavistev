from django.urls import path
from .views import home, crear_celular

urlpatterns = [
    path('', home, name="home"),
    path('crear-celular/', crear_celular, name="crear_celular"),
]