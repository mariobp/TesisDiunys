# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
import models as usuarios
from django.contrib.auth.models import User


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


class EgresadoForm(forms.ModelForm):

    class Meta:
        model = usuarios.Egresado
        fields = ['first_name', 'last_name', 'identificacion','email' ,'fecha_nacimiento', 'fecha_ingreso',
                  'fecha_egreso', 'celular', 'direccion', 'graduado']
    # end class

    def __init__(self, *args, **kwargs):
        super(EgresadoForm, self).__init__(*args, **kwargs)
        self.fields['identificacion'].help_text = "Este campo será usado como nombre de usuario y contraseña"
    # end def

    def clean_identificacion(self):
        identificacion = self.cleaned_data['identificacion']
        if identificacion:
            user = User.objects.filter(username=identificacion).first()
            egresado = usuarios.Egresado.objects.filter(identificacion=identificacion).first()
            if hasattr(self, 'instance') and self.instance.pk:
                if user.id != self.instance.id:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if egresado != self.instance:
                    raise forms.ValidationError('Ya existe un usuario con esta identificación')
                # end if
                return identificacion
            else:
                if user:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if egresado:
                    raise forms.ValidationError('Ya existe un usuario con esta identificación')
                # end if
                return identificacion
        # end if
        raise forms.ValidationError('Este campo es requerido')
    # end def

    def save(self, commit=False):
        usuario = super(EgresadoForm, self).save(commit)
        usuario.username = usuario.identificacion
        usuario.set_password(raw_password=usuario.identificacion)
        usuario.save()
        return usuario
    # end def
# end class


class EmpleadorForm(forms.ModelForm):

    class Meta:
        model = usuarios.Empleador
        fields = ['first_name', 'last_name', 'identificacion', 'email', 'fecha_nacimiento',
                  'celular', 'direccion', 'empresa', 'nit', 'cargo']
    # end class

    def __init__(self, *args, **kwargs):
        super(EmpleadorForm, self).__init__(*args, **kwargs)
        self.fields['nit'].help_text = "Este campo será usado como nombre de usuario y contraseña"
    # end def

    def clean_nit(self):
        nit = self.cleaned_data['nit']
        if nit:
            user = User.objects.filter(username=nit).first()
            egresado = usuarios.Empleador.objects.filter(nit=nit).first()
            if hasattr(self, 'instance') and self.instance.pk:
                if user.id != self.instance.id:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if egresado != self.instance:
                    raise forms.ValidationError('Ya existe un usuario con este nit')
                # end if
                return nit
            else:
                if user:
                    raise forms.ValidationError('Ya existe un usuario con este username')
                # end if
                if egresado:
                    raise forms.ValidationError('Ya existe un usuario con este nit')
                # end if
                return nit
        # end if
        raise forms.ValidationError('Este campo es requerido')
    # end def


    def save(self, commit=False):
        usuario = super(EmpleadorForm, self).save(commit)
        usuario.username = usuario.nit
        usuario.set_password(raw_password=usuario.nit)
        usuario.save()
        return usuario
    # end def
# end class


class DiligenciadorForm(forms.ModelForm):

    class Meta:
        model = usuarios.Diligenciador
        fields = ['email', 'celular', 'direccion']
    # end class
# end class
