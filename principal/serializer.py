from rest_framework import serializers
from .models import *

class usuarioSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Usuario
        # fields=('nombre','apellido','genero','correo','contraseña')
        fields='__all__'