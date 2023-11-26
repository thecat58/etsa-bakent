# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import *

class Post(models.Model):
    title = models.CharField(db_column='title', max_length=145)  # Field name made lowercase.
    body = models.CharField(db_column='body', max_length=145)  # Field name made lowercase.
    descripcion = models.ManyToManyField( User, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    def __str__(self):
        return str(self.title)
    class Meta:
        managed = True
        db_table = 'Post'


class Archivosadjuntos(models.Model):
    nombrearchivo = models.CharField(db_column='nombreArchivo', max_length=145)  # Field name made lowercase.
    rutaarchivo = models.CharField(db_column='rutaArchivo', max_length=145, blank=True, null=True)  # Field name made lowercase.
    materiales = models.ForeignKey('Materiales', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'archivosadjuntos'


class Categoriaservicio(models.Model):
    tipo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categoriaservicio'


class Citas(models.Model):
    id = models.IntegerField(primary_key=True)
    lugar = models.CharField(max_length=45, blank=True, null=True)
    agenda_id = models.IntegerField()
    agenda_taller_id = models.IntegerField()
    hora = models.TimeField(blank=True, null=True)
    asunto = models.CharField(max_length=160, blank=True, null=True)
    taller = models.ForeignKey('Taller', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'citas'


class Comentarios(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=160)
    puntuacion = models.DecimalField(max_digits=10, decimal_places=0)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    taller = models.ForeignKey('Taller', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'comentarios'


class Departamento(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'departamento'


class Materiales(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    fechacarga = models.DateField(db_column='fechaCarga', blank=True, null=True)  # Field name made lowercase.
    taller = models.ForeignKey('Taller', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'materiales'


class Municipio(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'municipio'


class Pagosuscripcion(models.Model):
    id = models.IntegerField(primary_key=True)
    tipopago = models.CharField(db_column='tipoPago', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'pagosuscripcion'


class Redessociales(models.Model):
    tiporedsocial = models.CharField(db_column='tipoRedSocial', max_length=100)  # Field name made lowercase.
    enlaceredsocial = models.CharField(db_column='enlaceRedSocial', max_length=45)  # Field name made lowercase.
    taller = models.ForeignKey('Taller', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'redessociales'


class Servicio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    categoriaservicio = models.ForeignKey(Categoriaservicio, models.DO_NOTHING)
    taller = models.ForeignKey('Taller', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'servicio'


class Taller(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ubicacion = models.CharField(max_length=160, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'taller'


class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    foto = models.CharField(max_length=45, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, models.DO_NOTHING)
    contrato_id = models.IntegerField()
    tpempresario_id = models.IntegerField()
    idcedula = models.IntegerField(blank=True, null=True)
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'usuario'
