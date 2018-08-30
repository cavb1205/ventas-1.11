# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Recaudos

@admin.register(Recaudos)
class RecaudosAdmin(admin.ModelAdmin):
    list_display = ('id_cartera','id_prestamo','valor','fecha_recaudo')
