# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Cartera(models.Model):
	responsable = models.ForeignKey(User,max_length=50,verbose_name='Responsable')
	celular = models.CharField(max_length=20,null=True,blank=True)
	direccion = models.CharField(max_length=50,null=True,blank=True)
	monto = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	ciudad = models.CharField(max_length=20)

	def __unicode__(self):
		mostrar="%s - %s  "%(self.id,self.responsable)
		return mostrar
