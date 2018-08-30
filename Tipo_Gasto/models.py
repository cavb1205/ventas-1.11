# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tipo_Gasto(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		mostrar="%s "%(self.nombre)
		return mostrar
