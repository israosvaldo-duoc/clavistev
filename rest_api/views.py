from django.shortcuts import render
from .serializers import CelularSerializer
from core.models import Celular
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Crud API (Completa) parte 1.
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
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

# Crud API (Completa) parte 2.
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def celular_2(request, pk):
        # Instanciar el elemento singular desde la bd
        try:
            celular = Celular.objects.get(idCelular=pk)
        except Celular.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Permite retornar un elemento desde la bd
        if request.method == 'GET':
            serializer = CelularSerializer(celular)
            return Response(serializer.data)
        # Permite actualizar un elemento desde la bd
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CelularSerializer(celular, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
        # Permite eliminar un elemento desde la bd
        elif request.method == 'DELETE':
            celular.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)