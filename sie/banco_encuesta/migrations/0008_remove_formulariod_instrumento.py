# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco_encuesta', '0007_auto_20170609_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulariod',
            name='instrumento',
        ),
    ]
