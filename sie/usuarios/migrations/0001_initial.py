# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 04:03
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identificacion', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Diligenciador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fecha_nacimiento', models.DateField()),
                ('identificacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Diligenciador',
                'verbose_name_plural': 'Diligenciadores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identificacion', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Egresado',
            fields=[
                ('diligenciador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.Diligenciador')),
                ('fecha_ingreso', models.DateField()),
                ('fecha_egreso', models.DateField()),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('usuarios.diligenciador',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Empleador',
            fields=[
                ('diligenciador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.Diligenciador')),
                ('empresa', models.CharField(max_length=100, verbose_name='Nombre empresa')),
                ('nit', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Empleador',
                'verbose_name_plural': 'Empleadores',
            },
            bases=('usuarios.diligenciador',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
