from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EgresadosE,Administradores,Perfil

class Egresados_Form(UserCreationForm):
	No_control=forms.CharField()
	Nombre_egresado=forms.CharField()
	App_egresado=forms.CharField()
	Apm_egresado=forms.CharField()
	Carrera=forms.CharField()
	Fecha_ingreso=forms.CharField()
	Fecha_egreso=forms.CharField()
	Correo=forms.EmailField()
	Foto=forms.ImageField()

class Perfil_Form(forms.ModelForm):
	class Meta():
		model=Perfil
		exclude=['NC_egresado']


class Administradores_Form(UserCreationForm):
	Correo=forms.EmailField()
	No_control=forms.CharField(max_length=12)
	Area=forms.CharField(max_length=30)