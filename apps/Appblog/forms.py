from django import forms
from ckeditor.fields import RichTextField
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.Form):

    titulo=forms.CharField()
    subtitulo=forms.CharField()
    slug=forms.CharField()
    descripcion=forms.CharField()
    autor=forms.ModelChoiceField(queryset=Autor.objects.all())
    categoria=forms.ModelChoiceField(queryset=Categoria.objects.all())
    cuerpo=forms.CharField()
    imagen_referencia=forms.ImageField(max_length=255)

#    imagen_referencia=forms.ImageField(upload_to='imagenes/', max_length=255,blank=True)
    publicado=forms.BooleanField(required=False)
    fecha_publicacion=forms.DateField(required=False)

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ['username','email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    
    