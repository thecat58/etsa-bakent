from pstats import Stats
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken


# Create your views here.

# token
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

#


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

    @api_view(['POST'])
    def update_items(request, pk):
        Citas = Citas.objects.get(pk=pk)
        data = CitasSerializer(instance=Citas, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=Stats.HTTP_404_NOT_FOUND)
