# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
import models as usuarios


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('Se ha producido un problema con tu nombre de usuario.', code='invalid_login')
    # end def
# end class


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
                  'last_name', 'identificacion', 'fecha_nacimiento', 'fecha_ingreso', 'fecha_egreso',
                  'celular', 'direccion', 'graduado']
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
                  'last_name', 'identificacion', 'fecha_nacimiento', 'fecha_ingreso', 'fecha_egreso',
                  'celular', 'direccion', 'graduado']
    # end class
# end class


class EmpleadorForm(UserCreationForm):

    class Meta:
        model = usuarios.Empleador
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'fecha_nacimiento',
                  'celular', 'direccion', 'empresa', 'nit']
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
                  'last_name', 'identificacion', 'fecha_nacimiento',
                  'celular', 'direccion', 'empresa', 'nit']
    # end class
# end class


class DiligenciadorForm(forms.ModelForm):

    class Meta:
        model = usuarios.Diligenciador
        fields = ['email', 'celular', 'direccion']
    # end class
# end class
