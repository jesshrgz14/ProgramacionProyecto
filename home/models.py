from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class EgresadosE(models.Model):
	CARRERAS=(
		('ISC','Ingenieria en Sistemas Computacionales'),
		('IEM','Ingenieria Electromecanica'),
		('IInd','Ingenieria Industrial'),
		('IInf','Ingenieria en Informatica'),
		)
	Usuario_egresado=models.OneToOneField(User)
	No_control=models.CharField(max_length=10,primary_key=True,unique=True)
	Nombre_egresado=models.CharField(max_length=20)
	App_egresado=models.CharField(max_length=20)
	Apm_egresado=models.CharField(max_length=20)
	Carrera=models.CharField(max_length=50,choices=CARRERAS)
	Fecha_ingreso=models.CharField(max_length=4)
	Fecha_egreso=models.CharField(max_length=4)
	Correo=models.EmailField()
	Foto = models.ImageField(upload_to='Egresados_Fotos', blank=True)
	class Meta:
		permissions = (
            ("editar_perfil", "Editar Perfil Usuario"),
            )


	def __unicode__(self):
		return "NC: %s - Nombre: %s - Apellido: %s "%(self.No_control,self.Nombre_egresado,self.App_egresado)

class Perfil(models.Model):
	NC_egresado=models.ForeignKey(EgresadosE)
	Titulado=models.BooleanField()
	Trabajo_Carrera=models.BooleanField()
	Empresa_trabajo=models.CharField(max_length=50,blank=True)
	Maestria=models.BooleanField()
	Maestria_descripcion=models.CharField(max_length=50,blank=True)
	Doctorado=models.BooleanField()
	Doctorado_descripcion=models.CharField(max_length=50,blank=True)
	Estudios_adicionales=models.TextField()
	Tiempo_trabajo=models.IntegerField()


	def __unicode__(self):
		return "NC: %s"%(self.NC_egresado)

class Administradores(models.Model):
	Usuario_admin=models.OneToOneField(User)
	Correo=models.EmailField()
	No_control=models.CharField(max_length=12)
	Area=models.CharField(max_length=30)
	class Meta:
		permissions = (
            ("admiistrador", "Administrador"),
            )

	def __unicode__(self):
		return "NC: %s- Correo: %s"%(self.No_control,self.Correo)

class BaseDatps(models.Model):
	NC=models.CharField(max_length=10)
	Nombre=models.CharField(max_length=25)
	Apellidos=models.CharField(max_length=50)

	def __unicode__(self):
		return "NC: %s - Nombre: %s - Apellidos: %s"%(self.NC,self.Nombre,self.Apellidos)
