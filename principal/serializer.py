from rest_framework import serializers
from .models import *

class usuarioSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Usuario
        # fields=('nombre','apellido','genero','correo','contraseña')
        fields='__all__'

class citasSerializers(serializers.ModelSerializers):
    class Meta:
        models=Citas
        fields='__all__'

class TallerSserializers(serializers.Modelserializers):
    class Meta:
        models=Taller
        fields='__all__'