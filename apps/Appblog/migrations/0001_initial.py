# Generated by Django 4.1 on 2022-09-30 02:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acerca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nosotros', models.TextField(verbose_name='Nosotros')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Acerca',
                'verbose_name_plural': 'Varios Acerca',
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la categoria')),
                ('imagen_referencia', models.ImageField(upload_to='categoria/', verbose_name='Imagen de Referencia')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre o Razon Social')),
                ('correo', models.EmailField(max_length=100, verbose_name='Email')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('web', models.CharField(max_length=100, verbose_name='Web')),
                ('mensaje', models.TextField(verbose_name='mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('titulo', models.CharField(max_length=100, unique=True, verbose_name='Titulo del Articulo')),
                ('subtitulo', models.CharField(max_length=100, unique=True, verbose_name='Subtitulo del Articulo')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Slug')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('cuerpo', ckeditor.fields.RichTextField()),
                ('imagen_referencia', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen de Referencia')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado / No Publicado')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicacion')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appblog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appblog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]