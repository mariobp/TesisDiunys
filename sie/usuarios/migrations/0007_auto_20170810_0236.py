# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20170809_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egresado',
            name='identificacion',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
