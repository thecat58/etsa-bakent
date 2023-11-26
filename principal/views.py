from django.shortcuts import render
<<<<<<< HEAD
from rest_framework.response import Response, viewsets
=======
>>>>>>> 5cf31727af9f3b7ca36536f4856693b348b5ab3c
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.decorators import action
from django.http import Http404
from rest_framework import viewsets

class postViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializers_class=postSerializers

<<<<<<< HEAD

# class  usuarioViewSet(viewsets.ModelViewSet):
#     queryset=Usuario.objects.all()
#     serializer_class=usuarioSerializers
class usuarioViewSet(APIView):
    # Método GET para obtener una lista de todos los clientes
    def get(self, request, format=None, *args, **kwargs):
        # Consulta a la base de datos para obtener todos los objetos Cliente
        post = Usuario.objects.all()
        # Serialización de los objetos Cliente en formato JSON
        serializer = usuarioSerializers(post, many=True)
        # Retorna una respuesta con los datos serializados
        return Response(serializer.data)

    # Método POST para crear un nuevo cliente
    def post(self, request, format=None):
        # Serialización de los datos del cliente proporcionados en la solicitud
        serializer = usuarioSerializers(data=request.data)
        if serializer.is_valid():
            # Guarda el nuevo cliente en la base de datos si la validación es exitosa
            serializer.save()
            # Retorna una respuesta con los datos del cliente creado y un código de estado 201 (CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna una respuesta con errores de validación y un código de estado 400 (BAD REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class citasViewSet(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Citas.objects.all()
        serializer = citasSerializers(post, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CitasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
    @action(methods=['post'],detail=True)
    def like_post(self, request, pk):
        post = self.get_objet()
>>>>>>> 5cf31727af9f3b7ca36536f4856693b348b5ab3c
