# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cartera


@admin.register(Cartera)
class CarteraAdmin(admin.ModelAdmin):
    list_display = ('responsable','celular','direccion','monto','ciudad')
