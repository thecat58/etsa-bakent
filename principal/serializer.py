from rest_framework import serializers
from .models import *


class postSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Usuario
        # fields=('nombre','apellido','genero','correo','contraseña')
        fields='__all__'

# Los serializadores definen la representación de la API.
class  CitasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'
