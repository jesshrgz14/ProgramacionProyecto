from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, UpdateView
from django.views.generic import FormView, ListView,DetailView
from django.core.urlresolvers import reverse_lazy
from .models import EgresadosE,Perfil,Administradores
from .forms import Egresados_Form,Perfil_Form,Administradores_Form

def Detalle_perfil(request,pk):
	r=Perfil.objects.get(NC_egresado=pk)
	return render(request,'perfil.html',{'list':r})

class EditarPerfilView(UpdateView):
	model=Perfil
	fields='__all__'
	template_name='editar_perfil.html'
	success_url=reverse_lazy('login')

class Consultas(ListView):
	template_name='consultas.html'
	model=EgresadosE

class Reportes(TemplateView):
	template_name='reportes.html'

class SignupEgresado(FormView):
	template_name='signup.html'
	form_class=Egresados_Form
	#no se ocupan los fields
	success_url=reverse_lazy('login')
	#se modifica el metodo valid
	def form_valid(self,form):
		user=form.save()
		p=EgresadosE()
		p.Usuario_egresado=user
		p.No_control=form.cleaned_data['No_control']
		p.Nombre_egresado=form.cleaned_data['Nombre_egresado']
		p.App_egresado=form.cleaned_data['App_egresado']
		p.Apm_egresado=form.cleaned_data['Apm_egresado']
		p.Carrera=form.cleaned_data['Carrera']
		p.Fecha_ingreso=form.cleaned_data['Fecha_ingreso']
		p.Fecha_egreso=form.cleaned_data['Fecha_egreso']
		p.Correo=form.cleaned_data['Correo']
		
		#campos
		p.save()
		return super(SignupEgresado, self).form_valid(form)

class SignupAdministrador(FormView):
	template_name='signup.html'
	form_class=Administradores_Form
	#no se ocupan los fields
	success_url=reverse_lazy('login')
	#se modifica el metodo valid
	def form_valid(self,form):
		user=form.save()
		p=Administradores()
		p.Usuario_admin=user
		p.Admon_nombre=form.cleaned_data['Admon_nombre']
		p.Admon_tel=form.cleaned_data['Admon_tel']
		p.Admon_correo=form.cleaned_data['Admon_correo']
		#campos
		p.save()
		return super(SignupAdministrador, self).form_valid(form)


class Crear_Perfil(CreateView):
	template_name='crear_perfil.html'
	model=Perfil
	fields='__all__'
	success_url=reverse_lazy('login')

