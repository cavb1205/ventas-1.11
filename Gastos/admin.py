# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Gastos

@admin.register(Gastos)
class GastosAdmin(admin.ModelAdmin):
    list_display = ('id_cartera','fecha_gasto','tipo_gasto','valor')
