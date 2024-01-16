from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.decorators import action
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.base_user import BaseUserManager
 
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  # Corregido el nombre del atributo

    @action(methods=['post'], detail=True)
    def like_post(self, request, pk):
        post = self.get_object()

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer


class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

    # Función personalizada para obtener todas las citas (GET)
    @action(detail=False, methods=['get'])
    def get_all_citas(self, request):
     citas = Citas.objects.all()
     serializer = CitasSerializer(citas, many=True)
     mensaje = 'Citas obtenidas exitosamente'
     return Response({'mensaje': mensaje, 'data': serializer.data})



    # Función personalizada para crear una nueva cita (POST)
    @action(detail=False, methods=['post'])
    def create_cita(self, request):
        serializer = CitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Función personalizada para crear una nueva cita (POST)
    @action(detail=False, methods=['post'])
    def create_cita(self, request):
        serializer = CitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Cita creada exitosamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'mensaje': 'Error al crear la cita', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Función personalizada para actualizar una cita (PUT)
    @action(detail=True, methods=['put'])
    def update_cita(self, request, pk=None):
        cita = self.get_object()
        serializer = CitasSerializer(cita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Cita actualizada exitosamente', 'data': serializer.data})
        return Response({'mensaje': 'Error al actualizar la cita', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Función personalizada para eliminar una cita (DELETE)
    @action(detail=True, methods=['delete'])
    def delete_cita(self, request, pk=None):
        cita = self.get_object()
        cita.delete()
        return Response({'mensaje': 'Cita eliminada exitosamente'})

    # Función que devuelve una respuesta personalizada para cualquier método
    @action(detail=False, methods=['get', 'post', 'put', 'delete'])
    def custom_response(self, request):
        data = {'mensaje': 'su accion fue realizada correctamente'}
        return Response(data)