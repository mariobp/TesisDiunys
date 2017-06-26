# -*- coding: utf-8 -*-
from django import forms
from cuser.middleware import CuserMiddleware
import models
from encuesta.models import Opcion
from usuarios.models import Diligenciador


class FormularioDForm(forms.ModelForm):

    class Meta:
        model = models.FormularioD
        exclude = ('diligenciador',)
    # end class

    def clean(self):
        user = CuserMiddleware.get_user()
        diligenciador = Diligenciador.objects.filter(id=user.pk).first()
        if diligenciador:
            return super(FormularioDForm, self).clean()
        # end if
        raise forms.ValidationError(
            "Este usuario no es de tipo diligenciador")
    # end def

    def save(self, commit=False):
        d = super(FormularioDForm, self).save(commit)
        user = CuserMiddleware.get_user()
        diligenciador = Diligenciador.objects.filter(id=user.pk).first()
        d.diligenciador = diligenciador
        d.save()
        # end if
        return d
    # end def
# end class


class AsignacionEgresadoForm(forms.ModelForm):

    class Meta:
        model = models.AsignarEncuestaEgresado
        exclude = ()
    # end class

    def __init__(self, *args, **kwargs):
        super(AsignacionEgresadoForm, self).__init__(*args, **kwargs)
        self.fields['instrumento'].queryset = self.fields['instrumento'].queryset.filter(tipo=False)
        self.fields['instrumento'].widget.can_add_related = False
        self.fields['instrumento'].widget.can_change_related = False
    # end def
# end clas


class AsignacionEmpleadorForm(forms.ModelForm):

    class Meta:
        model = models.AsignarEncuestaEmpleador
        exclude = ()
    # end class

    def __init__(self, *args, **kwargs):
        super(AsignacionEmpleadorForm, self).__init__(*args, **kwargs)
        self.fields['instrumento'].queryset = self.fields['instrumento'].queryset.filter(tipo=True)
        self.fields['instrumento'].widget.can_add_related = False
        self.fields['instrumento'].widget.can_change_related = False
    # end def
# end class
