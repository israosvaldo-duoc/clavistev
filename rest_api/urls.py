from core.models import Celular
from django.urls import path
from .views import  celular_1, celular_2

urlpatterns = [
    path('celular/', celular_1, name='celular_1'),
    path('celular/<pk>', celular_2, name='celular_2')
]