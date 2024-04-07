from rest_framework import serializers
from django.contrib.auth.models import *
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password


from principal.models import *


# token pedorro
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('nombre',)

class MunicipioSerializer(serializers.ModelSerializer):
    departamento_id = DepartamentoSerializer(read_only=True)

    class Meta:
        model = Municipio
        fields = '__all__'


class IdentificacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tdocumento
        fields = '__all__'
class CustomTokenResponseSerializer(serializers.ModelSerializer):
    tipodocumento = IdentificacionModelSerializer(read_only=True)
    municipio = MunicipioSerializer(read_only=True)
    class Meta:
        model = Usuario
        fields = '__all__'

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
        
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(
                request= self._context.get('request'),
                username = email,
                password = password
            )  

            if not user:
                raise serializers.ValidationError('Credenciales incorrectas')
            
            data['user'] = user
        else:
            raise serializers.ValidationError('complete los campos')
        return data
    
# Serializador de Departamento


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        # Asegurarse de que la contraseña se encripta antes de guardar el usuario
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    def update(self, instance, validated_data):
        update_user=super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
 


# fon de esa chimbada 

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'primer_nombre')

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'




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
    taller_reseptor_id = serializers.PrimaryKeyRelatedField(queryset=Taller.objects.all(), source='taller_reseptor')
    usuario_author_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), source='usuario_author')

    class Meta:
        model = Citas
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['taller_reseptor'] = TallerSerializer(instance.taller_reseptor).data
        representation['usuario_author'] = UserModelSerializer  (instance.usuario_author).data
        return representation