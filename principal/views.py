from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.decorators import action
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets



class postViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializers_class=postSerializers


    @action(methods=['post'],detail=True)
    def like_post(self, request, pk):
        post = self.get_objet()

    
class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

    # Ejemplo de un método personalizado para obtener todas las citas
    @action(detail=False, methods=['get'])
    def get_all_citas(self, request):
        citas = Citas.objects.all()
        serializer = CitasSerializer(citas, many=True)
        return Response(serializer.data)

    # Método de creación de una nueva cita
    @action(detail=False, methods=['post'])
    def create_cita(self, request):
        serializer = CitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

