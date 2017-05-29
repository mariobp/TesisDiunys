# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import models as usuarios


class AdministradorForm(UserCreationForm):

    class Meta:
        model = usuarios.Administrador
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'fecha_nacimiento']
    # end class

    def save(self, commit=True):
        usuario = super(AdministradorForm, self).save(commit)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save()
        return usuario
    # end def
# end class


class AdministradorFormEdit(forms.ModelForm):

    class Meta:
        model = usuarios.Administrador
        fields = ['username', 'email', 'first_name',
                  'last_name', 'identificacion', 'fecha_nacimiento']
    # end class
# end class


class DirectorForm(UserCreationForm):

    class Meta:
        model = usuarios.Director
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'cargo', 'fecha_nacimiento']
    # end class

    def save(self, commit=True):
        usuario = super(DirectorForm, self).save(commit)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save()
        return usuario
    # end def
# end class


class DirectorEdit(forms.ModelForm):

    class Meta:
        model = usuarios.Director
        fields = ['username', 'email', 'first_name',
                  'last_name', 'identificacion', 'cargo', 'fecha_nacimiento']
    # end class
# end class


class EgresadoForm(UserCreationForm):

    class Meta:
        model = usuarios.Egresado
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'fecha_nacimiento', 'fecha_ingreso', 'fecha_egreso', 'graduado']
    # end class

    def save(self, commit=True):
        usuario = super(EgresadoForm, self).save(commit)
        usuario.save()
        return usuario
    # end def
# end class


class EgresadoEdit(forms.ModelForm):

    class Meta:
        model = usuarios.Egresado
        fields = ['username', 'email', 'first_name',
                  'last_name', 'identificacion', 'fecha_nacimiento', 'fecha_ingreso', 'fecha_egreso', 'graduado']
    # end class
# end class


class EmpleadorForm(UserCreationForm):

    class Meta:
        model = usuarios.Empleador
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'fecha_nacimiento', 'empresa', 'nit']
    # end class

    def save(self, commit=True):
        usuario = super(EmpleadorForm, self).save(commit)
        usuario.save()
        return usuario
    # end def
# end class


class EmpleadorFormEdit(forms.ModelForm):

    class Meta:
        model = usuarios.Empleador
        fields = ['username', 'email', 'first_name',
                  'last_name', 'identificacion', 'fecha_nacimiento', 'empresa', 'nit']
    # end class
# end class
