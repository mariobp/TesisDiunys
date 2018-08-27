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
        
        if len(emails) is not 0:
            subject, from_email, to = "Encuesta", 'egresadosprosistemas@gmail.com', emails
            text_content = "Encuesta académica"
            html_content = """
                <p>Estimado Egresado.</p>
                <p>Teniendo en cuenta la política de mejoramiento constante en la Universidad de Cartagena, 
                primera institución pública de la Región Caribe con Acreditación Institucional; es necesario brindar 
                los espacios adecuados para la participación de usted como egresado en la construcción de una universidad
                con altos estándares de calidad y que impacte positivamente el sector empresarial; por lo cual el Programa 
                de Ingeniería de Sistemas lo a participar activamente en este proceso de retroalimentación que busca el 
                crecimiento institucional.</p>

                <p>Es importante para nosotros contar con su colaboración en el diligenciamiento de una pequeña encuesta que 
                medirá la percepción del programa a partir de su posición como egresado del Programa de Ingeniería de Sistemas 
                de la Universidad de Cartagena; con base en los resultados obtenidos, se logrará la construcción de planes de mejoramiento.</p>

                <p>Este instrumento de medición es aplicado de forma digital por medio de una plataforma llamada SIE, 
                para acceder siga las siguientes instrucciones</p>

                <p>A través del link: <a href="http://sie.seedprojects.org" target="_blank">sie.seedprojects.org</a></p>
                <ul>
                    <li>
                        Usuario: CEDULA DE CIUDADANIA sin guiones, puntos o espacios
                    </li>
                    <li>
                        Contraseña: CEDULA DE CIUDADANIA sin guiones, puntos o espacios
                    </li>
                </ul>

                <p>Al ingresar debes aceptar los términos sobre el manejo de información con fines académicos, 
                las preguntas son de selección múltiple con única respuesta, de existir dos posibles respuestas a una pregunta, 
                seleccione la más acertada o con mayor valor según su criterio.</p>

                <p>Para cualquier duda, información o aclaración que considere necesaria, se pueden comunicar con el docente Plinio Puello Marrugo 
                por medio de su correo ppuellom@unicartagena.edu.co o al del Programa de Ingeniería de Sistemas pringsistemas@unicartagena.edu.co.</p>

                <p>Se agradece de antemano su colaboración.</p>
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
                <p>Respetado empleador.</p>
                <p>Teniendo en cuenta la política de mejoramiento constante en la Universidad de Cartagena, 
                primera institución pública de la Región Caribe con Acreditación Institucional; es necesario brindar 
                los espacios adecuados para la participación de nuestros aliados estratégicos en la construcción de una 
                universidad con altos estándares de calidad y que impacte positivamente el sector empresarial; por lo cual 
                el Programa de Ingeniería de Sistemas invita a su empresa para participar activamente en este proceso de 
                retroalimentación que busca el crecimiento institucional.</p>

                <p>Es importante para nosotros contar con su colaboración y la de su empresa, para participar en el diligenciamiento 
                de una pequeña encuesta que medirá la percepción del programa a partir de la opinión del sector externo donde se emplean
                los practicantes del Programa de Ingeniería de Sistemas de la Universidad de Cartagena; con base en los resultados obtenidos,
                se logrará la construcción de planes de mejoramiento.</p>

                <p>Este instrumento de medición es aplicado de forma digital por medio de una plataforma llamada SIE, 
                para acceder siga las siguientes instrucciones</p>

                <p>A través del link: <a href="http://sie.seedprojects.org" target="_blank">sie.seedprojects.org</a></p>
                <ul>
                    <li>
                       Usuario: correo electrónico.
                    </li>
                    <li>
                       Contraseña: correo electrónico. 
                    </li>
                </ul>

                <p>Al ingresar debes aceptar los términos sobre el manejo de información con fines académicos, 
                las preguntas son de selección múltiple con única respuesta, de existir dos posibles respuestas a una pregunta, 
                seleccione la más acertada o con mayor valor según su criterio.</p>

                <p>Para cualquier duda, información o aclaración que considere necesaria, se pueden comunicar con el docente Plinio Puello Marrugo 
                por medio de su correo ppuellom@unicartagena.edu.co o al del Programa de Ingeniería de Sistemas pringsistemas@unicartagena.edu.co.</p>

                <p>Cordialmente</p>

                <p>Ing. Luis Carlos Tovar Garrido <br>Director <br>Programa de Ingeniería de Sistemas</p>
                <p>Ing. Luis A. Garcia Zapateiro <br>Decano (e) <br>Facultad de Ingeniería</p>
            """
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(unicode(html_content, encoding='utf-8'), "text/html")
            msg.attach_file('media/Empleadores.pdf')
            msg.send()
        # end if
    # end if
#end def
