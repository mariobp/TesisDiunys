# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='egresado',
            options={'verbose_name': 'Egresado', 'verbose_name_plural': 'Egresados'},
        ),
    ]
