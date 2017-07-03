# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Pregunta(models.Model):
    enunciado = models.TextField()
    numero = models.IntegerField()

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

    def __unicode__(self):
        return u'%s' % (self.texto)
    # end def
# end class


class Instrumento(models.Model):
    opciones = (
        (False, "Egresado"),
        (True, "Empleador")
    )
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    preguntas = models.ManyToManyField(Cerrada)
    tipo = models.BooleanField(default=False, choices=opciones)

    class Meta:
        verbose_name = "Instrumento"
        verbose_name_plural = "Instrumentos"
    # end class

    def descargar_datos(self):
        return '<a href="/banco/export/xls/%d/">Exportar Datos</a>' % (self.pk)
    # end def

    descargar_datos.allow_tags = True

    def estadisticas(self):
        return '<a href="#" onclick="data(%d)">Estadisticas</a>' % (self.pk)
    # end def

    estadisticas.allow_tags = True

    def __unicode__(self):
        return unicode(self.nombre)
    # end def
# end class
