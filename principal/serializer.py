from rest_framework import serializers
from django.contrib.auth.models import *

from principal.models import (Post,Citas, Usuario)



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'primer_nombre')


class PostSerializer(serializers.ModelSerializer):
    likes = UserModelSerializer(many=True, read_only=True)
    author = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    is_liked=serializers.SerializerMethodField()

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('id','title','body','likes', 'author','like_count','is_liked')

    def get_author(self, obj):
        return obj.author.primer_nombre

    def get_like_count(self, obj):  # Corregido el nombre del método
        return len(obj.likes.all())

    def get_is_liked(self, obj):
        Usuario = self.context['request'].Usuario
        return True if Usuario in obj.likes.all() else False

# fin notificaciones




class CitasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'
