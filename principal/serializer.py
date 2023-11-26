from rest_framework import serializers
from .models import *

class postSerializers(serializers.ModelSerializer):
    class Meta: 
<<<<<<< HEAD
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
=======
        model=Post
>>>>>>> 5cf31727af9f3b7ca36536f4856693b348b5ab3c
        fields='__all__'