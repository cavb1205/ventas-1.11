# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Cartera.models import Cartera

BOOL_CHOICES = ((True, 'Activo'),(False, 'Inactivo'))
class Usuarios(models.Model):
	documento = models.IntegerField(unique=True,verbose_name='Documento')
	nombres = models.CharField(max_length=30,verbose_name='Nombres')
	apellidos = models.CharField(max_length=30,verbose_name='Apellidos')
	telefono = models.CharField(max_length=20,null=True,blank=True)
	celular = models.CharField(max_length=20,null=True,blank=True)
	direccion = models.CharField(max_length=50,null=True,blank=True)
	ingreso_mensual = models.DecimalField(verbose_name='Ingresos Mensuales',max_digits=10,decimal_places=2,null=True,blank=True)
	id_cartera = models.ForeignKey(Cartera,verbose_name='Almacen')
	estado = models.BooleanField(default=True,choices=BOOL_CHOICES,verbose_name='Estado')


	def __unicode__(self):
		mostrar="%s - %s "%(self.nombres,self.apellidos)
		return mostrar


