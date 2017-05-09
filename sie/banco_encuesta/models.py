# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios import models as usuarios
from encuesta import models as encuesta
# Create your models here.


class FormularioD(models.Model):
    instrumento = models.ForeignKey(encuesta.Instrumento)
    diligenciador = models.ForeignKey(usuarios.Diligenciador)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Formulario Digilenciado"
        verbose_name_plural = "Formularios Digilenciados"
    # end class

    def __unicode__(self):
        return u'%s' % (self.instrumento)
    # end def
# end class


class Respuesta(models.Model):
    encuesta = models.ForeignKey(FormularioD)

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
    # end class
# end class


class Cerrada(Respuesta):
    pregunta = models.ForeignKey(encuesta.Cerrada)
    respuestas = models.ManyToManyField(encuesta.Opcion)

    class Meta:
        verbose_name = "Respuesta Cerrada"
        verbose_name_plural = "Respuestas Cerradas"
    # end class
# end class


class Otros(Respuesta):
    pregunta = models.ForeignKey(encuesta.Cerrada)
    respuesta = models.TextField("¿Otro? ¿Cual?")

    class Meta:
        verbose_name = "Respuesta Otro"
        verbose_name_plural = "Respuestas Otro"
    # end class
# end class
