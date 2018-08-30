# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Tipo_Gasto.models import Tipo_Gasto
from Cartera.models import Cartera

class Gastos(models.Model):
	fecha_gasto = models.DateField(auto_now=False,verbose_name='Fecha del Gasto')
	tipo_gasto = models.ForeignKey(Tipo_Gasto)
	valor = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Valor')
	observaciones = models.CharField(max_length=100,verbose_name='Observaciones')
	id_cartera = models.ForeignKey(Cartera,verbose_name='Almacen')

	def __unicode__(self):
		mostrar="%s - %s  "%(self.fecha_gasto,self.valor)
		return mostrar
