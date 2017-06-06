# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class InterfazConfig(ModuleMixin, AppConfig):
    name = 'interfaz'
    icon = '<i class="material-icons">flight_takeoff</i>'
