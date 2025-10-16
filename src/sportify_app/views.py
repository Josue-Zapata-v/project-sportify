from rest_framework import viewsets, filters
from .models import Equipo, Jugador
from .serializers import EquipoSerializer, JugadorSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'categoria']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Equipo eliminado correctamente"}, status=status.HTTP_200_OK)
    
class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
