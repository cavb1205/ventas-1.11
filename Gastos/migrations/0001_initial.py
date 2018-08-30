# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cartera', '0001_initial'),
        ('Tipo_Gasto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_gasto', models.DateField(verbose_name='Fecha del Gasto')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('observaciones', models.CharField(max_length=100, verbose_name='Observaciones')),
                ('id_cartera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartera.Cartera', verbose_name='Almacen')),
                ('tipo_gasto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tipo_Gasto.Tipo_Gasto')),
            ],
        ),
    ]