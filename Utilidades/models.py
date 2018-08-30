# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Cartera.models import Cartera

class Utilidades(models.Model):
	fecha_entrega = models.DateField(auto_now=False,verbose_name='Fecha de Entrega')
	valor_utilidad = models.DecimalField(verbose_name='Valor de la Utilidad',max_digits=10,decimal_places=2)
	descripcion = models.CharField(verbose_name='Descripción',max_length=100)
	id_cartera = models.ForeignKey(Cartera,verbose_name='Almacen')

	def __unicode__(self):
		mostrar="%s - %s  "%(self.fecha_entrega,self.valor_utilidad)
		return mostrar
