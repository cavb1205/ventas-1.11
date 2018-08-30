# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Utilidades


@admin.register(Utilidades)
class UtilidadesAdmin(admin.ModelAdmin):
    list_display = ('id_cartera','fecha_entrega','valor_utilidad')
