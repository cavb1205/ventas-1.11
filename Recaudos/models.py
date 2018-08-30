# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Cartera.models import Cartera
from Prestamos.models import Prestamos

class Recaudos(models.Model):
	fecha_recaudo = models.DateField(auto_now=False)
	valor = models.DecimalField(verbose_name='Valor del Abono',max_digits=10,decimal_places=2)
	id_cartera = models.ForeignKey(Cartera,verbose_name='Almacen')
	id_prestamo = models.ForeignKey(Prestamos,verbose_name='Abonar a Venta')

	def __unicode__(self):
		mostrar="%s - %s - %s "%(self.id_prestamo_id,self.fecha_recaudo, self.valor)
		return mostrar
