# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 11:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.EmailField(max_length=254)),
                ('No_control', models.CharField(max_length=12)),
                ('Area', models.CharField(max_length=30)),
                ('Usuario_admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EgresadosE',
            fields=[
                ('No_control', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Nombre_egresado', models.CharField(max_length=20)),
                ('App_egresado', models.CharField(max_length=20)),
                ('Apm_egresado', models.CharField(max_length=20)),
                ('Carrera', models.CharField(choices=[('ISC', 'Ingenieria en Sistemas Computacionales'), ('IEM', 'Ingenieria Electromecanica'), ('IInd', 'Ingenieria Industrial'), ('IInf', 'Ingenieria en Informatica')], max_length=50)),
                ('Fecha_ingreso', models.CharField(max_length=4)),
                ('Fecha_egreso', models.CharField(max_length=4)),
                ('Correo', models.EmailField(max_length=254)),
                ('Usuario_egresado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulado', models.BooleanField()),
                ('Trabajo_Carrera', models.BooleanField()),
                ('Empresa_trabajo', models.CharField(blank=True, max_length=50)),
                ('Maestria', models.BooleanField()),
                ('Maestria_descripcion', models.CharField(blank=True, max_length=50)),
                ('Doctorado', models.BooleanField()),
                ('Doctorado_descripcion', models.CharField(blank=True, max_length=50)),
                ('Estudios_adicionales', models.TextField()),
                ('Tiempo_trabajo', models.IntegerField()),
                ('NC_egresado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.EgresadosE')),
            ],
        ),
    ]
