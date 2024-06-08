import re
from django import forms
from .models import *
from django.contrib.auth.models import User, Group

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_contacto', 'correo_contacto', 'telefono_contacto', 'mensaje_contacto', 'tipos_contacto']
        widgets = {
            'mensaje_contacto': forms.Textarea(attrs={
                'rows': 5,
                'style': 'resize: none; width: 100%;'
            }),
        }

    def clean_telefono_contacto(self):
        telefono = self.cleaned_data.get('telefono_contacto')
        if telefono and len(telefono.replace(" ", "")) != 9:
            raise forms.ValidationError("El número de teléfono debe tener exactamente 9 dígitos.")
        return telefono
    def clean_correo_contacto(self):
        correo = self.cleaned_data.get('correo_contacto')
        if correo:
            # Expresión regular para validar un correo electrónico
            correo_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(correo_regex, correo):
                raise forms.ValidationError("Por favor, ingrese un correo electrónico válido.")
        return correo

class AlumnosForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Datos_Alumnos
        fields = "__all__"       
        widgets = {
            'password': forms.PasswordInput(),
            'confirmar_password': forms.PasswordInput(),
        }

class ModeradorForm(forms.ModelForm):
    class Meta:
        model = Datos_Moderador
        fields = "__all__"     
        widgets = {
            'password': forms.PasswordInput(),
            'confirmar_password': forms.PasswordInput(),
        }
    apellido_Moderador = forms.CharField(max_length=50)

class PublicacionForm (forms.ModelForm):
    class Meta: 
        model = PostAlumnos
        fields = ['nombre_post', 'descripcion_post',  'imagen_post']
        widgets = {
            'descripcion_post': forms.Textarea(attrs={
                'rows': 5,
                'style': 'resize: none; width: 100%;'
            }),}

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombreEquipo', 'descripcion', 'imagen']

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'autor', 'descripcion', 'categoria', 'fecha_publicacion', 'archivo_libro', 'portada']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control mx-auto',  # Agregamos mx-auto para centrar
                'style': 'resize:none; width:230px; height:150px;',
            }),
        }




class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario aquí...',
                'style': 'width: 100%; height: 120px; resize: none;'  # Fijar el tamaño y desactivar redimensionamiento
            }),
        }
        labels = {
            'contenido': 'Comentario',
        }