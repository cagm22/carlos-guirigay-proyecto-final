
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post,Avatar
from .forms import AvatarForm, PostForm, UserRegisterForm, UserEditForm, AvatarForm
import random
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class Inicio(ListView):
    def get(self, request, *args, **kwargs):
        posts = list(Post.objects.filter(
            estado= True,
            publicado= True
            ))
        print(posts)
        
#        posts=random.choice(Post.objects.all())
        print('---------------------posts-------------------------------------------')
        print(posts)
        print('----------------------------------------------------------------')

        post1=random.choice(posts)
        posts.remove(post1)

        post2=random.choice(posts)
        posts.remove(post2)
        post3=random.choice(posts)
        posts.remove(post3)
        post4=random.choice(posts)
        posts.remove(post4)

        contexto= {
            'post1': post1,
            'post2': post2,
            'post3': post3,
            'post4': post4,
        }



        return render(request, 'index.html', contexto)



# class Inicio(ListView):
#     def get(self, request, *args, **kwargs):
#         posts = list(Post.objects.filter(
#             estado= True,
#             publicado= True
#             ))
#         post1=random.choice(Post.objects.all())
#         posts.remove(post1)
#         post2=random.choice(posts)
#         posts.remove(post2)
#         post3=random.choice(posts)
#         posts.remove(post3)
#         post4=random.choice(posts)
#         posts.remove(post4)

#         contexto= {
#             'post1': post1,
#             'post2': post2,
#             'post3': post3,
#             'post4': post4,
#         }

#         return render(request, 'index.html', contexto)



class ListadoPosts(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):
        lista_posts= Post.objects.filter(
                    estado= True,
                    publicado= True,
                    )
        contexto={
            'lista_posts': lista_posts,
        }
        
        return render(request, 'lista_posts.html', contexto)

class About(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')

class Indice(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'indice.html')

class DetallePost(DetailView):
    def get(self, request,slug, *args, **kwargs):
        try:
            post=Post.objects.get(slug=slug)
        except:
            post=None
        contexto={
            'post': post,
        }
        return render(request,'detalle_post.html',contexto)

@login_required
def PostFormulario(request):
        if request.method == 'POST':
            miFormulario=PostForm(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                info=miFormulario.cleaned_data

                post=Post(
                    titulo=info['titulo'],subtitulo=info['subtitulo'],slug=info['slug'],descripcion=info['descripcion'], 
                    autor=info['autor'],categoria=info['categoria'],cuerpo=info['cuerpo'], publicado=info['publicado'],
                    fecha_publicacion=info['fecha_publicacion']
                        )
                print(post)
                post.save()
                return render(request, 'postformulario.html')

        else:
            miFormulario=PostForm()
        return render(request, 'postformulario.html', {"miFormulario":miFormulario, "avatar":obtenerAvatar(request)})


def eliminarPost(request, post_titulo):
    post=Post.objects.get(titulo=post_titulo)
    post.delete()

    post=Post.objects.all()
    contexto={'post':post}
    return render(request, 'lista_posts.html',contexto)


def editarPost(request, post_titulo):
    post=Post.objects.get(titulo=post_titulo)
    print('----------------------------------------------------------------')
    print(post_titulo)
    print('----------------------------------------------------------------')
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            post.titulo=info['titulo']
            post.subtitulo = info['subtitulo']
            post.slug= info['slug']
            post.descripcion = info['descripcion']
            post.autor = info['autor']
            post.categoria = info['categoria']
            post.cuerpo = info['cuerpo']
            post.fecha_publicacion = info['fecha_publicacion']
            post.save()
            post=Post.objects.all()
            return render(request, 'lista_posts.html', {"post":post})


    else:
        print('----------------------ELSE------------------------------')

        form=PostForm(initial={'titulo':post.titulo,'subtitulo':post.subtitulo,'slug':post.slug,'descripcion':post.descripcion, 
                    'autor':post.autor,'categoria':post.categoria,'cuerpo':post.cuerpo,
                    'fecha_publicacion':post.fecha_publicacion})
        print('----------------------FORM------------------------------')

        return render(request, 'editarPost.html', {'formulario':form, 'post':post, "avatar":obtenerAvatar(request)})

def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'editarPerfil.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'login.html', {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, 'login.html', {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})


    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'formulario':form})

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, 'index.html', {'mensaje':f"Usuario {username} creado correctamente"})
        else:
            return render(request, 'register.html', {"formulario":form, "mensaje":"Formulario invalido"})


    else:
        form=UserRegisterForm()
        return render(request, 'register.html', {"formulario":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method == 'POST':
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email= info['email']
            usuario.password1= info['password1']
            usuario.password2= info['password2']
            usuario.save()
            return render(request, 'index.html', {'mensaje':"Perfil editado correctamente"})
        else:
            return render(request, 'editarPerfil.html', {"formulario":form, "usuario":usuario, "mensaje":"Formulario Invalido", "avatar":obtenerAvatar(request)})

    else:
        form=UserEditForm(instance=usuario)


#    lista=Avatar.objects.filter(user=request.user)
#    if len(lista)!=0:
#        avatar=lista[0].imagen.url
#    else:
#        avatar=""

    return render(request, 'editarPerfil.html', {"formulario":form, "usuario":usuario, "avatar":obtenerAvatar(request)})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():

            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo[0].delete()


            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'editarPerfil.html', {'usuario':request.user, 'mensaje':'Avatar Agregado con Exito', "imagen":avatar.imagen.url})
        else:
            return render(request, 'agregarAvatar.html', {"formulario":formulario, 'mensaje':'Formulario Invalido'})
    else:
        formulario=AvatarForm()
        return render(request, 'agregarAvatar.html', {"formulario":formulario, "usuario":request.user, "avatar":obtenerAvatar(request)})

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatar-default.png"
    return imagen