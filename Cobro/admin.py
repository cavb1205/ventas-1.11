# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cobro


@admin.register(Cobro)
class CobroAdmin(admin.ModelAdmin):
    list_display = ('id_cartera','fecha','valor')
