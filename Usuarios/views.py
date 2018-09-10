# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Usuarios
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class UsuariosList(ListView):
    model = Usuarios

class UsuariosDetail(DetailView):
    model = Usuarios

class UsuariosCreation(CreateView):
    model = Usuarios
    success_url = reverse_lazy('usuarios:list')
    fields = ['documento','nombres','apellidos','telefono','celular','direccion','id_cartera','estado']

class UsuariosUpdate(UpdateView):
    model = Usuarios
    success_url = reverse_lazy('usuarios:list')
    fields = ['documento','nombres','apellidos','telefono','celular','direccion','id_cartera','estado']

class UsuariosDelete(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuarios:list')