from rest_framework import serializers
from .models import Equipo, Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['id', 'nombre', 'posicion', 'numero_camiseta', 'equipo']

class EquipoSerializer(serializers.ModelSerializer):
    jugadores = JugadorSerializer(many=True, read_only=True) 

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'ciudad', 'categoria', 'jugadores']
