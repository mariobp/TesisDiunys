# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco_encuesta', '0011_auto_20170620_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariod',
            name='asignacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_encuesta.AsignarEncuesta', verbose_name='Asignaci\xf3n'),
        ),
    ]