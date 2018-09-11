# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Cartera
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class CarteraList(ListView):
    model = Cartera

class CarteraDetail(DetailView):
    model = Cartera

class CarteraCreation(CreateView):
    model = Cartera
    success_url = reverse_lazy('cartera:list')
    fields = ['responsable','celular','direccion','monto','ciudad']

class CarteraUpdate(UpdateView):
    model = Cartera
    success_url = reverse_lazy('cartera:list')
    fields = ['responsable','celular','direccion','monto','ciudad']

class CarteraDelete(DeleteView):
    model = Cartera
    success_url = reverse_lazy('cartera:list')