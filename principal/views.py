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

    # Ejemplo de un método personalizado para obtener todas las citas
    # @action(methods=['post'], detail=True)
    # def like_post(self, request, pk):
    #         post = self.get_object()