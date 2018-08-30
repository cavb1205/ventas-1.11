# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Cartera.models import Cartera

class Cobro(models.Model):
	fecha = models.DateField(auto_now=False)
	valor = models.DecimalField(max_digits=10,decimal_places=2)
	id_cartera = models.ForeignKey(Cartera)
		
