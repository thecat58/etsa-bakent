from crypt import methods
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.decorators import action
from django.http import Http404


class PostioViewSet(APIView):
    queryset= Post=object.all()
    serializers_class=postSerializers

    @action(methods['post'],delail=True)
    def like_post(self, request, pk):
        post = self.get_objet()