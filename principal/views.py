from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.decorators import action
from django.http import Http404
from rest_framework import viewsets

class postViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializers_class=postSerializers

    @action(methods=['post'],detail=True)
    def like_post(self, request, pk):
        post = self.get_objet()