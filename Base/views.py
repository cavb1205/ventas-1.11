# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Base
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class BaseList(ListView):
    model = Base

class BaseDetail(DetailView):
    model = Base

class BaseCreation(CreateView):
    model = Base
    success_url = reverse_lazy('bases:list')
    fields = ['fecha_entrega','valor','observaciones','id_cartera']

class BaseUpdate(UpdateView):
    model = Base
    success_url = reverse_lazy('bases:list')
    fields = ['fecha_entrega','valor','observaciones','id_cartera']

class BaseDelete(DeleteView):
    model = Base
    success_url = reverse_lazy('bases:list')