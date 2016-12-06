"""proyectoE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from django.conf import settings
from home.views import SignupEgresado,Detalle_perfil,EditarPerfilView,Consultas,Reportes,Crear_Perfil


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login, {'template_name':'index.html'},name='login'),
    url(r'^salir/$',logout_then_login,name='logout'),  
    url(r'^signup/$', SignupEgresado.as_view(), name='signup_view'),
    url(r'^editar/(?P<pk>\d+)$', EditarPerfilView.as_view(), name='edit_view'),
    url(r'^perfil/(?P<pk>\d+)$', Detalle_perfil, name='perfil_view'),
    url(r'^consulta/$', Consultas.as_view(), name='consulta_view'),
    url(r'^reportes/$', Reportes.as_view(), name='reporte_view'),
    url(r'^crear_perfil/$', Crear_Perfil.as_view(), name='crearperfil_view'),
]
