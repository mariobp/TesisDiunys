# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Pregunta(models.Model):
    enunciado = models.CharField(max_length=100)
    numero = models.IntegerField()
    estado = models.BooleanField(default=True, help_text="Indica si esta habilitada")

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
    # end class

    def __unicode__(self):
        return u'%s' % (self.enunciado)
    # end def
# end class


class Cerrada(Pregunta):
    multiple = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pregunta Cerrada"
        verbose_name_plural = "Preguntas Cerradas"
    # end class
# end class


class Opcion(models.Model):
    pregunta = models.ForeignKey(Cerrada)
    texto = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Opcion"
        verbose_name_plural = "Opciones"
    # end class

    def pregunta_id(self):
        return pregunta.id
    # end def

    def __unicode__(self):
        return u'%s %s' % (self.pregunta, self.texto)
    # end def
# end class


class Instrumento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    preguntas = models.ManyToManyField(Cerrada)

    class Meta:
        verbose_name = "Instrumento"
        verbose_name_plural = "Instrumentos"
    # end class

    def descargar_datos(self):
        return "<a>Datos</a>"
    # end def

    def estadisticas(self):
        return "Graficos"
    # end def

    descargar_datos.allow_tags = True

    def __unicode__(self):
        return unicode(self.nombre)
    # end def
# end class
