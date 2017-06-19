# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20170619_2240'),
        ('banco_encuesta', '0009_auto_20170619_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignarEncuestaEgresado',
            fields=[
                ('asignarencuesta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='banco_encuesta.AsignarEncuesta')),
                ('egresados', models.ManyToManyField(to='usuarios.Egresado')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.GrupoPeriodo')),
            ],
            options={
                'verbose_name': 'Asignaci\xf3n de encuesta egresado',
                'verbose_name_plural': 'Asignaciones de encuesta a egresados',
            },
            bases=('banco_encuesta.asignarencuesta',),
        ),
        migrations.CreateModel(
            name='AsignarEncuestaEmpleador',
            fields=[
                ('asignarencuesta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='banco_encuesta.AsignarEncuesta')),
                ('empleadores', models.ManyToManyField(to='usuarios.Empleador')),
            ],
            options={
                'verbose_name': 'Asignaci\xf3n de encuesta empleador',
                'verbose_name_plural': 'Asignaciones de encuesta a empleadores',
            },
            bases=('banco_encuesta.asignarencuesta',),
        ),
    ]
