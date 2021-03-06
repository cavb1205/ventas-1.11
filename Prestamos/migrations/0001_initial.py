# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cartera', '0001_initial'),
        ('Plazos', '0001_initial'),
        ('Usuarios', '0001_initial'),
        ('Estado_Prestamo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(verbose_name='Fecha de Venta')),
                ('monto_inicial', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto Inicial')),
                ('interes', models.IntegerField(default=20)),
                ('cuotas', models.IntegerField(default=24)),
                ('valor_cuota', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Cuota')),
                ('total_pagar', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total a Pagar')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('saldo_actual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_prestamo', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Estado_Prestamo.Estado_Prestamo', verbose_name='Estado Venta')),
                ('id_cartera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cartera.Cartera', verbose_name='Almacen')),
                ('id_usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Usuarios', verbose_name='Cliente')),
                ('plazos', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Plazos.Plazos')),
            ],
        ),
    ]
