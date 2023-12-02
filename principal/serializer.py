from rest_framework import serializers
from django.contrib.auth.models import *
from .models import *

class UserSerializer(serializers.ModelSerializer):
    model = User
fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)  # Asumo que UserSerializer es tu serializer para los usuarios
    author = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    is_liked=serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_author(self, obj):
        return obj.author.username

    def get_like_count(self, obj):  # Corregido el nombre del método
        return len(obj.likes.all())
    
    def get_is_liked(self, obj):  
        user=self.context['request'].user
        return True if user in obj.likes.all() else False
    
# fin notificaciones

# Los serializadores definen la representación de la API.
class  CitasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'
