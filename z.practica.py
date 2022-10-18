"""
1. creamos el proyecto
2. creamos la app
3. creamos los modelos
4. agregamos los modelos en la DB
.creamos el superuser: python3 manage.py createsuperuser
.en app/admin.py agregamos los modelos que queremos en el panel Admin: 
    from . models import *
    admin.site.register(MODELO)
. Para agregar imagenes desde panel Admin a nuestros modelos que lo soliciten 
creamos un lugar llamado media en settings.py ademas lo agregamos a urls.py, 
tambien creamos la carpeta media en la base del directorio
    MEDIA_URL = '/media/'
    MEDIA_ROOT=BASE_DIR / 'media'
        en urls.py
        urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
. para Agregar el template que vamos a usar en el proyecto, creamos una carpeta "templates"
en la base del directorio y dentro copiamos los html, y las carpetas img, js etc, en static, 
y reparamos los links del html padre para que usen la nueva ubicacion de los img, js, css, etc






"""