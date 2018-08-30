# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Prestamos

@admin.register(Prestamos)
class PrestamosAdmin(admin.ModelAdmin):
    list_display = ('id_cartera','id_usuarios','fecha_prestamo','monto_inicial','interes','cuotas','valor_cuota','total_pagar','fecha_vencimiento','saldo_actual','estado_prestamo')
