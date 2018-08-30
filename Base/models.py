# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Cartera.models import Cartera

class Base(models.Model):
	fecha_entrega = models.DateField(auto_now=False)
	valor = models.DecimalField( verbose_name='Valor',max_digits=10,decimal_places=2)
	observaciones = models.CharField(verbose_name='Observaciones',max_length=100)
	id_cartera = models.ForeignKey(Cartera, verbose_name='Almacen')

	def __unicode__(self):
		mostrar="%s "%(self.id_cartera)
		return mostrar
