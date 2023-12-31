from rest_framework import serializers
from django.contrib.auth.models import *
from django.contrib.auth import get_user_model, authenticate


from principal.models import (Post,Citas, Taller, Usuario)


# token pedorro


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
        
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request= self._context.get('request'),
            username = email,
            password = password
        )  

        if not user:
            raise serializers.ValidationError('Credenciales incorrectas')
        
        data['user'] = user
        
        return data


# fon de esa chimbada 

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



class TallerSerializer(serializers.ModelSerializer):
    dueñp_taller = UserModelSerializer(read_only=True)

    class Meta:
        model = Taller
        fields = '__all__'

class CitasSerializer(serializers.ModelSerializer):
    taller_receptor = TallerSerializer(read_only=True)

    class Meta:
        model = Citas
        fields = '__all__'