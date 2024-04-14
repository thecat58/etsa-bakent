# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from principal.manage import AuthUserManager
from django.dispatch import receiver
import os
from django.db import models

class SeederStatus(models.Model):
    seeds_applied = models.BooleanField(default=False)


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'departamento'

    def __str__(self):
        txt = '{0}'
        return txt.format(self.nombre)


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    departamento_id = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, null=True, related_name='departamento_id')

    class Meta:
        managed = True
        db_table = 'municipio'

    def __str__(self):
        txt = '{0}'
        return txt.format(self.nombre)


class Tdocumento(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tdocumento'

    def __str__(self):
        txt = '{0}'
        return txt.format(self.nombre)


class Usuario(AbstractBaseUser, PermissionsMixin):
    primer_nombre = models.CharField(max_length=45)
    segundo_nombre = models.CharField(max_length=45, blank=True, null=True)
    primer_apellido = models.CharField(max_length=45, null=True)
    segundo_apellido = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=120, null=True)
    telefono = models.CharField(max_length=20, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    fechanacimiento = models.DateField(
        db_column='fechaNacimiento', blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios', null=True)
    n_identificacion = models.IntegerField(unique=True, null=True)
    tipodocumento = models.ForeignKey(
        Tdocumento, on_delete=models.CASCADE,  null=True, related_name='tipodocumento')
    municipio = models.ForeignKey(
        Municipio, on_delete=models.CASCADE,  null=True, related_name='municipio')
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    vededor = models.BooleanField(default=False)

    # Establecer los campos groups y user_permissions como nulos

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['primer_nombre', 'primer_apellido', 'n_identificacion']

    class Meta:
        managed = True
        db_table = 'Usuario'



class Taller(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='taller', null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ubicacion = models.CharField(max_length=160, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    usuriotaller = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, related_name='dueñp_taller')

    class Meta:
        managed = True
        db_table = 'taller'

    def __str__(self):
        return self.nombre

@receiver(models.signals.post_delete, sender=Taller)
def auto_delete_file_(sender, instance, **kwargs):
    """
    Elimina el archivo de imagen asociado cuando se elimina un objeto Taller.
    """
    if instance.foto:
        if os.path.isfile(instance.foto.path):
            os.remove(instance.foto.path)


class Categoriaservicio(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categoriaservicio'


class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    categoriaservicio = models.ForeignKey(Categoriaservicio, models.DO_NOTHING)
    id_taller = models.ForeignKey(
        Taller, on_delete=models.CASCADE, null=True, related_name='id_taller')

    class Meta:
        managed = True
        db_table = 'servicio'


class Materiales(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    fechacarga = models.DateField(
        db_column='fechaCarga', blank=True, null=True)
    material_taller = models.ForeignKey(
        Taller, on_delete=models.CASCADE, null=True, related_name='material_taller')

    class Meta:
        managed = True
        db_table = 'materiales'


class Archivosadjuntos(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Field name made lowercase.
    nombrearchivo = models.CharField(db_column='nombreArchivo', max_length=145)
    # Field name made lowercase.
    rutaarchivo = models.CharField(
        db_column='rutaArchivo', max_length=145, blank=True, null=True)
    materiales_adjuntos = models.ForeignKey(
        Materiales, on_delete=models.CASCADE, null=True, related_name='materiales_adjuntos')

    class Meta:
        managed = True
        db_table = 'archivosadjuntos'


class Redessociales(models.Model):
    id = models.AutoField(primary_key=True)
    # Field name made lowercase.
    tiporedsocial = models.CharField(db_column='tipoRedSocial', max_length=100)
    # Field name made lowercase.
    enlaceredsocial = models.CharField(
        db_column='enlaceRedSocial', max_length=45)
    taller_redsocial = models.ForeignKey(
        Taller, on_delete=models.CASCADE, null=True, related_name='taller_redsocial')

    class Meta:
        managed = True
        db_table = 'redessociales'


class Citas(models.Model):
    id = models.AutoField(primary_key=True)
    lugar = models.CharField(max_length=45, blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    asunto = models.CharField(max_length=160, blank=True, null=True)
    taller_reseptor = models.ForeignKey(
        Taller, on_delete=models.CASCADE, null=True, related_name='taller_reseptor')
    usuario_author = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, related_name='usuario_author')

    class Meta:
        managed = True
        db_table = 'citas'


class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=160)
    puntuacion = models.DecimalField(max_digits=10, decimal_places=0)
    reptor_taller = models.ForeignKey(
        Taller, on_delete=models.CASCADE, null=True, related_name='reptor_taller')
    ahutor = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, related_name='ahutor')

    class Meta:
        managed = True
        db_table = 'comentarios'


class Pagosuscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    # Field name made lowercase.
    tipopago = models.CharField(
        db_column='tipoPago', max_length=45, blank=True, null=True)
    usuario_id = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, related_name='usuario_id')

    class Meta:
        managed = True
        db_table = 'pagosuscripcion'


class Post(models.Model):
    # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=145)
    # Field name made lowercase.
    body = models.CharField(db_column='body', max_length=145)
    likes = models.ManyToManyField(Usuario, blank=True)
    author = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return str(self.title)

    class Meta:
        managed = True
