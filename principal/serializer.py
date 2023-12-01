from rest_framework import serializers
from django.contrib.auth.models import *
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta: 
        model=User
        # fields=('nombre','apellido','genero','correo','contraseña')
        fields='__all__'


class postSerializers(serializers.ModelSerializer):
    likes= UserSerializers(many=True, read_only=True)
    author= serializers.SerializerMethodField()
    like_
    
    class Meta: 
        model=Post
        # fields=('nombre','apellido','genero','correo','contraseña')
        fields='__all__'
    
    def get_author(self,obj):
        return obj.author.username

# Los serializadores definen la representación de la API.
class  CitasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'
