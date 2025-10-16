from rest_framework import viewsets, filters
from .models import Equipo, Jugador
from .serializers import EquipoSerializer, JugadorSerializer

# Create your views here.
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'categoria']
