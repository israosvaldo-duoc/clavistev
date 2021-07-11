from django.db.models import fields
from rest_framework import serializers
from core.models import Celular

class CelularSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Celular
        fields = ['idCelular', 'marca', 'modelo', 'compania']