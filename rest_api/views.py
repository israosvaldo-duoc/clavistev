from django.shortcuts import render
from .serializers import CelularSerializer
from core.models import Celular
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
# Create your views here.

def celular_1(request):
    # Permite listar todos los celulares
    if request.method == 'GET':
        celular_lista = Celular.objects.all()
        serializer = CelularSerializer(celular_lista, many=True)
        return Response(serializer.data)
    # Permite agregar un celular desde la API    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CelularSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

#def celular_2(request):    