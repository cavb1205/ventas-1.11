# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Plazos(models.Model):
	nombre = models.CharField(max_length=20)

	def __unicode__(self):
		mostrar="%s"%(self.nombre)
		return mostrar
