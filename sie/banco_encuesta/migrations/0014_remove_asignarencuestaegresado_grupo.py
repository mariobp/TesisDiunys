# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-20 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco_encuesta', '0013_auto_20170809_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignarencuestaegresado',
            name='grupo',
        ),
    ]
