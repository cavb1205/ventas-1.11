# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Gastos
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class GastosList(ListView):
    model = Gastos

class GastosDetail(DetailView):
    model = Gastos

class GastosCreation(CreateView):
    model = Gastos
    success_url = reverse_lazy('gastos:list')
    fields = ['fecha_gasto','tipo_gasto','valor','observaciones','id_cartera']

class GastosUpdate(UpdateView):
    model = Gastos
    success_url = reverse_lazy('gastos:list')
    fields = ['fecha_gasto','tipo_gasto','valor','observaciones','id_cartera']

class GastosDelete(DeleteView):
    model = Gastos
    success_url = reverse_lazy('gastos:list')