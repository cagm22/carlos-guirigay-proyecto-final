from django.urls import path
from .views import Inicio, ListadoPosts, About, Indice, DetallePost, PostFormulario, eliminarPost, editarPost, login_request, register, editarPerfil, agregarAvatar
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',Inicio.as_view(), name='index'),
    path('pages/',ListadoPosts.as_view(), name='lista_posts'),
    path('about/',About.as_view(), name='about'),
    path('indice/',Indice.as_view(), name='indice'),
    path('postformulario/',PostFormulario, name='postformulario'),
    path('eliminarPost/<post_titulo>',eliminarPost, name='eliminarPost'),
    path('editarPost/<post_titulo>',editarPost, name='editarPost'),
    
    path('login/',login_request, name='login'),
    path('register/',register, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    
    
    
    
    
    
    
    path('<slug:slug>/',DetallePost.as_view(), name='detalle_post'),

]