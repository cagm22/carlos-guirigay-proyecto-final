from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class ModeloBase(models.Model):
    id=models.AutoField(primary_key=True)
    estado=models.BooleanField('Estado',default=True)
    fecha_creacion=models.DateField('Fecha de creacion',auto_now=False,auto_now_add=True)
    fecha_modificacion=models.DateField('Fecha de modificacion',auto_now=True,auto_now_add=False)
    fecha_eliminacion=models.DateField('Fecha de eliminacion',auto_now=True,auto_now_add=False)

    class Meta:
        abstract=True

class Categoria(ModeloBase):
    nombre=models.CharField('Nombre de la categoria',max_length=100, unique=True)
    imagen_referencia=models.ImageField('Imagen de Referencia',upload_to='categoria/')

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.nombre

class Autor(ModeloBase):
    nombre=models.CharField('Nombres',max_length=100)
    apellidos=models.CharField('Apellidos',max_length=100)
    email=models.EmailField('Correo',max_length=100)
    descripcion=models.TextField('Descripcion')
    web=models.URLField('Web', null=True,blank=True)

    class Meta:
        verbose_name="Autor"
        verbose_name_plural="Autores"

    def __str__(self):
        return self.nombre+ " " +str(self.apellidos)

class Post(ModeloBase):
    titulo=models.CharField('Titulo del Articulo',max_length=100, unique=True,blank=True,null=True)
    subtitulo=models.CharField('Subtitulo del Articulo',max_length=100, unique=True,blank=True,null=True)
    slug=models.CharField('Slug',max_length=100, unique=True,blank=True,null=True)
    descripcion=models.TextField('Descripcion',blank=True,null=True)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE,blank=True,null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE,blank=True,null=True)
    cuerpo=RichTextField(blank=True,null=True)
    imagen_referencia=models.ImageField('Imagen de Referencia', upload_to='imagenes/', max_length=255,blank=True)
    publicado=models.BooleanField('Publicado / No Publicado',default=False,blank=True,null=True)
    fecha_publicacion=models.DateField('Fecha de publicacion',blank=True,null=True)


    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"

    def __str__(self):
        return self.titulo+ " " +str(self.categoria)

class Acerca(ModeloBase):
    nosotros=models.TextField('Nosotros')
    telefono=models.CharField('Telefono',max_length=15)
    email=models.EmailField('Email',max_length=100)
    direccion=models.CharField('Direccion',max_length=200)

    class Meta:
        verbose_name="Acerca"
        verbose_name_plural="Varios Acerca"

    def __str__(self):
        return self.nosotros

class Contacto(ModeloBase):
    nombre=models.CharField('Nombre o Razon Social',max_length=100)
    correo=models.EmailField('Email',max_length=100)
    asunto=models.CharField('Asunto',max_length=100)
    web=models.CharField('Web',max_length=100)
    mensaje=models.TextField('mensaje')

    class Meta:
        verbose_name="Contacto"
        verbose_name_plural="Contactos"

    def __str__(self):
        return self.nombre+ " " +str(self.asunto)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares/', null=True, blank=True)

#    def __str__(self):
#        return self.user