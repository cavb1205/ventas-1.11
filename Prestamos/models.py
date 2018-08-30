# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Plazos.models import Plazos
from Estado_Prestamo.models import Estado_Prestamo
from Cartera.models import Cartera
from Usuarios.models import Usuarios

class Prestamos(models.Model):
	fecha_prestamo = models.DateField(auto_now=False,verbose_name='Fecha de Venta')
	monto_inicial = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Monto Inicial')
	interes = models.IntegerField(default=20)
	cuotas = models.IntegerField(default=24)
	plazos = models.ForeignKey(Plazos,default='1')
	valor_cuota = models.DecimalField(verbose_name='Valor Cuota',max_digits=10,decimal_places=2)
	total_pagar = models.DecimalField(verbose_name='Total a Pagar',max_digits=10,decimal_places=2,blank=True,null=True)
	fecha_vencimiento = models.DateField(verbose_name='Fecha de Vencimiento')
	saldo_actual = models.DecimalField(max_digits=10,decimal_places=2)
	observaciones = models.CharField(max_length=100,null=True,blank=True)
	estado_prestamo = models.ForeignKey(Estado_Prestamo,default='1',verbose_name='Estado Venta')
	id_cartera = models.ForeignKey(Cartera,verbose_name='Almacen')
	id_usuarios = models.ForeignKey(Usuarios,verbose_name='Cliente')

	def __unicode__(self):
		mostrar="%s "%(self.id_usuarios)
		return mostrar

	def dias_restantes(self):
		cuota=self.saldo_actual/self.valor_cuota
		return cuota

	def dias_pagos(self):
		dias_pagos = (self.total_pagar-self.saldo_actual)/self.valor_cuota
		return dias_pagos

	def total_pago(self):
		total_pago = (self.total_pagar-self.saldo_actual)
		return total_pago
