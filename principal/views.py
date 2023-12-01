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
        Post = self.get_objet()

    
class CitasViewSet(viewsets.ModelViewSet):
    def get(self, request, format=None, *args, **kwargs):
        citas = Citas.objects.all()
        serializer = CitasSerializer(citas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

