# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Estado_Prestamo


@admin.register(Estado_Prestamo)
class Estado_PrestamoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
