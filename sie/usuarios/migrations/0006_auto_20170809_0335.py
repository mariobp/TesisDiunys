# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_empleador_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diligenciador',
            name='identificacion',
        ),
        migrations.AddField(
            model_name='egresado',
            name='identificacion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleador',
            name='identificacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='egresado',
            name='graduado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='empleador',
            name='nit',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
