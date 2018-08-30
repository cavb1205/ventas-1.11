# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Base


@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display = ('id_cartera','fecha_entrega','valor')
