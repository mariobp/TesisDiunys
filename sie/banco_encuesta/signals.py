#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from django.core.mail import EmailMultiAlternatives
import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@receiver(post_save, sender=models.AsignarEncuestaEgresado)
def enviarCorreoEgresados(sender, instance, **kwargs):
    asignacion = models.AsignarEncuestaEgresado.objects.filter(id=instance.id).first()
    emails = []
    if asignacion:
        for e in asignacion.egresados.all():
            emails.append(e.email)
        # end for
        if asignacion.grupo:
            for g in asignacion.grupo.egresados.all():
                emails.append(g.email)
            # end for
        # end if
        if len(emails) is not 0:
            subject, from_email, to = "Encuesta", 'egresadosprosistemas@gmail.com', emails
            text_content = "Encuesta académica"
            html_content = """
                <p>Te invitamos a participar en el proyecto de grado “Herramienta informática para apoyar los medios de
                participación del egresado del programa de Ingeniería de Sistemas de la Universidad de Cartagena”.</p>

                <p>A través del link. <a href="http://sie.seedprojects.org" target="_blank">sie.seedprojects.org</a></p>
                <p>Ingresando con:</p>
                <ul>
                    <li>
                       Usuario: CEDULA DE IDENTIFICACION sin espacios o puntos.
                    </li>
                    <li>
                       Contraseña: CEDULA DE IDENTIFICACION sin espacios o puntos.
                    </li>
                </ul>

                <p>Al ingresar debes aceptar los términos, y contestar la encuesta de la manera más objetiva posible.</p>

                <p>Con esta información apoyaras al fortalecimiento de las relaciones
                de los egresados y empleadores con el Programa y la participación
                de los mismos en los procesos de autoevaluación y mejoramiento continuo.</p>
                <p>¡Gracias!</p>
            """
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(unicode(html_content, encoding='utf-8'), "text/html")
            msg.send()
        # end if
    # end if
# end def


@receiver(post_save, sender=models.AsignarEncuestaEmpleador)
def enviarCorreoEmpleador(sender, instance, **kwargs):
    asignacion = models.AsignarEncuestaEmpleador.objects.filter(id=instance.id).first()
    emails = []
    if asignacion:
        for e in asignacion.empleadores.all():
            emails.append(e.email)
        # end for

        if len(emails) is not 0:
            subject, from_email, to = "Encuesta académica Universidad de Cartagena", 'egresadosprosistemas@gmail.com', emails
            text_content = "Encuesta académica"
            html_content = """
                <p>Te invitamos a participar en el proyecto de grado “Herramienta informática para apoyar los medios de
                participación del egresado del programa de Ingeniería de Sistemas de la Universidad de Cartagena”.</p>

                <p>A través del link. <a href="http://sie.seedprojects.org" target="_blank">sie.seedprojects.org</a></p>
                <p>Ingresando con:</p>
                <ul>
                    <li>
                       Usuario: NIT de la empresa que representas sin guiones, espacios o puntos.
                    </li>
                    <li>
                       Contraseña: NIT de la empresa que representas sin guiones, espacios o puntos.
                    </li>
                </ul>

                <p>Al ingresar debes aceptar los términos, y contestar la encuesta de la manera más objetiva posible.</p>

                <p>Con esta información apoyaras al fortalecimiento de las relaciones
                de los egresados y empleadores con el Programa y la participación
                de los mismos en los procesos de autoevaluación y mejoramiento continuo.</p>
                <p>¡Gracias!</p>
            """
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(unicode(html_content, encoding='utf-8'), "text/html")
            msg.send()
        # end if
    # end if
#end def
