# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dia

@admin.register(Dia)
class DiaAdmin(admin.ModelAdmin):
    list_display = ('id_cartera','fecha','valor')
