# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Estado_Prestamo(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		mostrar="%s"%(self.nombre)
		return mostrar
