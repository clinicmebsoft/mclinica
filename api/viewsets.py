from django.shortcuts import get_object_or_404
from rest_framework import viewsets


from personal.models import Doctores,Especialidad
from citas.models import Cita
from inventarios.models import Articulos
from rest_framework.decorators import action

from api.serializer import EspecialidadesSerializer
from api.serializer import DoctoresSerializer
from api.serializer import CitaSerializer
from api.serializer import ArticulosSerializer
from rest_framework.response import Response


class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadesSerializer

    @action(detail=True, methods=['get'])
    def lista_especialidad(self, request, pk=None):
        queryset = Doctores.objects.filter(especialidad=pk)
        serializer = DoctoresSerializer(queryset, many=True)

        return Response(serializer.data)

class DoctoresViewSet(viewsets.ModelViewSet):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer


    '''
    def list(self, request):
        queryset = Doctores.objects.all()
        serializer = DoctoresSerializer(queryset, many=True)
        return Response(serializer.data)

    #metodo para obtener el detalle de un elemento
    def retrieve(self, request, pk=None):
        queryset = Doctores.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DoctoresSerializer(user)
        return Response(serializer.data)
        '''

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulos.objects.all()
    serializer_class = ArticulosSerializer