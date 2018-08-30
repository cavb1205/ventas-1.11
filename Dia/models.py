# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Cartera.models import Cartera

class Dia(models.Model):
	fecha = models.DateField(auto_now=False)
	valor = models.DecimalField(max_digits=10,decimal_places=2)
	id_cartera = models.ForeignKey(Cartera)

	def __unicode__(self):
		mostrar="%s - %s  "%(self.fecha,self.valor)
		return mostrar
