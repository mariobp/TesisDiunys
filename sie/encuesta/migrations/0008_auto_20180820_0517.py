# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-20 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0007_auto_20180820_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcion',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='opciones',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='encuesta.Opcion'),
            preserve_default=False,
        ),
    ]
