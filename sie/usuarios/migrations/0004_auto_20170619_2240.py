# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20170529_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='diligenciador',
            name='celular',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='diligenciador',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Direcci\xf3n'),
        ),
    ]