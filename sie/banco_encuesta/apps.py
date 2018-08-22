# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class BancoEncuestaConfig(AppConfig):
    name = 'banco_encuesta'
    icon = '<i class="material-icons">assessment</i>'
    verbose_name = 'Medición'

    def ready(self):
        import signals
