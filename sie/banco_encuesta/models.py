# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios import models as usuarios
from encuesta import models as encuesta
# Create your models here.


class AsignarEncuesta(models.Model):
    instrumento = models.ForeignKey(encuesta.Instrumento)
    diligenciadores = models.ManyToManyField(usuarios.Diligenciador)
    grupo = models.ForeignKey(usuarios.GrupoPeriodo, blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Asignación de Encuesta"
        verbose_name_plural = "Asignaciones de Encuesta"
    # end class

    def __unicode__(self):
        return u"%s %s" % (self.instrumento.nombre, self.fecha.strftime("%Y-%m-%d"))
# end class


class FormularioD(models.Model):
    asignacion = models.ForeignKey(AsignarEncuesta)
    diligenciador = models.ForeignKey(usuarios.Diligenciador)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Formulario Digilenciado"
        verbose_name_plural = "Formularios Digilenciados"
    # end class

    def __unicode__(self):
        return u'%s' % (self.asignacion.instrumento)
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
