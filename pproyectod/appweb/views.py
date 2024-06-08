from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
from .models import *
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib import messages
import os
# Create your views here.


#error 404

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, "home.html")
@login_required(login_url='/accounts/login/')
def baseContacto(request):
    return render(request, "home.html")

@login_required(login_url='/accounts/login/')
def homeAdmin(request):
    return render(request, "homeAdmin.html")

@login_required(login_url='/accounts/login/')
def homeAlumno(request):
    return render(request, "homeAlumno.html")


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')  # Cambia 'alguna_vista' por la vista a la que quieres redirigir
    else:
        formulario = ContactoForm()
    return render(request, 'contacto.html', {'form_contacto': formulario})

@login_required(login_url='/accounts/login/')
def gestionar_contactos(request):
    contactos = Contacto.objects.all()

    if request.method == 'POST':
        contacto_id = request.POST.get('contacto_id')
        contacto = get_object_or_404(Contacto, id=contacto_id)
        
        if 'estado' in request.POST:
            contacto.estado = request.POST['estado']
            contacto.save()
        elif 'eliminar' in request.POST:
            contacto.delete()

        return redirect('gestionar_contactos')

    return render(request, 'gestionar_contactos.html', {'contactos': contactos})

def login_usuario(request):
    username = request.user.username
    print("Bienvenido " + username)
    
    # Mostrar SweetAlert según el tipo de usuario
    if request.user.groups.filter(name='alumno').exists():
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como alumno.')
        return redirect('homeAlumno')
    elif request.user.groups.filter(name='moderador').exists():
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como moderador.')
        return redirect('homeModerador')
    else:
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como administrador.')
        return redirect('homeAdmin')

#def login_usuario(request):
    username = request.user.username
    print("Bienvenido " + username)
    
    # Mostrar SweetAlert según el tipo de usuario
    if request.user.groups.filter(name='alumno').exists():
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como alumno.')
    elif request.user.groups.filter(name='moderador').exists():
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como moderador.')
    else:
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como administrador.')
    
    # Redirigir al usuario a la página de inicio correspondiente
    if request.user.groups.filter(name='alumno').exists():
        return redirect('homeAlumno')
    elif request.user.groups.filter(name='moderador').exists():
        return redirect('homeModerador')
    else:
        return redirect('homeAdmin')





def registroUsuarios(request):
    data = {'formAl': AlumnosForm}

    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirmar_password = form.cleaned_data.get('confirmar_password')

            if password != confirmar_password:
                messages.error(request, "Las contraseñas no coinciden.")
                return render(request, 'registration/registroUsuarios.html', data)
            else:
                rut = form.cleaned_data.get('rut_Usuario')
                nombre = form.cleaned_data.get('nombre_Usuario')
                apellido = form.cleaned_data.get('apellido_Usuario')
                telefono = form.cleaned_data.get('telefono_Usuario')
                carrera = form.cleaned_data.get('carrera_Usuario')
                semestre = form.cleaned_data.get('semestre_Usuario')
                correo = form.cleaned_data.get('correo')

                if User.objects.filter(email=correo).exists():
                    messages.error(request, "El correo ya se encuentra registrado.")
                    return render(request, 'registration/registroUsuarios.html', data)
                else:
                    usu = User.objects.create_user(username=nombre, email=correo, password=password, first_name=nombre, last_name=apellido)
                    grupo = Group.objects.get(name='alumno')
                    usu.groups.add(grupo)

                    alumno = Datos_Alumnos.objects.create(
                        rut_Usuario=rut,
                        nombre_Usuario=nombre,
                        apellido_Usuario=apellido,
                        telefono_Usuario=telefono,
                        carrera_Usuario=carrera,
                        semestre_Usuario=semestre,
                        correo=correo,
                        password=password
                    )
                    messages.success(request, "Usuario creado con éxito")
                    return redirect(reverse("login"))

    return render(request, "registration/registroUsuarios.html", data)


@login_required(login_url='/accounts/login/')
def inicioAdmin(request):
    return render(request,"baseAdmin.html")


@login_required(login_url='/accounts/login/')
def inicioAlumno(request):
    return render(request, "baseAlumno.html")



@login_required(login_url='/accounts/login/')
def inicioModerador(request):
    return render(request, "baseModerador.html")

@login_required(login_url='/accounts/login/')
def homeModerador(request):
    return render(request, "homeModerador.html")

@login_required(login_url='/accounts/login/')
def registroUsuariosAdmin(request):
    data = {'formModerador': ModeradorForm}

    if request.method == 'POST':
        form = ModeradorForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirmar_password = form.cleaned_data.get('confirmar_password')

            if password != confirmar_password:
                messages.error(request, "Las contraseñas no coinciden.")
                return render(request, 'registration/registroUsuarios.html', data)
            else:
                nombre_moderador = form.cleaned_data.get('nombre_Moderador')
                apellido_moderador = form.cleaned_data.get('apellido_Moderador')  # Obtener el apellido del formulario
                rut_moderador = form.cleaned_data.get('rut_Moderador')
                telefono_Moderador = form.cleaned_data.get('telefono_Moderador')
                correo = form.cleaned_data.get('correo')

                if User.objects.filter(email=correo).exists():
                    messages.error(request, "El correo ya se encuentra registrado.")
                    return render(request, 'registration/registroUsuarios.html', data)
                else:
                    usu = User.objects.create_user(username=nombre_moderador, email=correo, password=password, first_name=nombre_moderador, last_name=apellido_moderador)
                    grupo = Group.objects.get(name='moderador')
                    usu.groups.add(grupo)

                    moderador = form.save()  # Guardar el moderador en la base de datos

                    messages.success(request, "Usuario creado con éxito")
                    return redirect(reverse("homeAdmin"))

    return render(request, "mantenedor/registroUsuariosAdmin.html", data)


@login_required(login_url='/accounts/login/')
def postAlumnos(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Publicación enviada con éxito!')
            return redirect('homeAlumno')
        else:
            messages.error(request, '¡Ha ocurrido un error al enviar la publicación!')
    else:
        form = PublicacionForm()

    data = {
        'formPost': form,
    }
    return render(request, "postAlumno.html", data)




@login_required(login_url='/accounts/login/')
def publicaciones(request):
    queryset = request.GET.get("buscar")
    
    if queryset:
        publicaciones = PostAlumnos.objects.filter(
            Q(nombre_post__icontains=queryset) |
            Q(descripcion_post__icontains=queryset),
            estado='aprobado'
        ).distinct()
        mensaje = None
    else:
        publicaciones = PostAlumnos.objects.filter(estado='aprobado')
        mensaje = "No se encontraron publicaciones con esa búsqueda."

    success_message = None

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = get_object_or_404(PostAlumnos, pk=request.POST.get("publicacion_id"))
            comentario.autor = request.user
            comentario.save()
            success_message = "Tu comentario ha sido enviado con éxito."
            return render(request, 'publicaciones.html', {
                "publicaciones": publicaciones,
                "mensaje": mensaje,
                "form": form,
                "success_message": success_message
            })
    else:
        form = ComentarioForm()

    data = {
        "publicaciones": publicaciones,
        "mensaje": mensaje,
        "form": form,
        "success_message": success_message
    }

    return render(request, 'publicaciones.html', data)

@login_required(login_url='/accounts/login/')
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.user == comentario.autor:
        comentario.delete()
        return redirect('publicaciones')
    else:
        return redirect('publicaciones')

def es_moderador(user):
    return user.is_staff

@login_required(login_url='/accounts/login/')
def moderar_publicaciones(request):
    publicaciones_pendientes = PostAlumnos.objects.filter(estado='pendiente')
    return render(request, 'moderar_publicaciones.html', {'publicaciones': publicaciones_pendientes})


@login_required(login_url='/accounts/login/')
def aprobar_publicacion(request, pk):
    publicacion = get_object_or_404(PostAlumnos, pk=pk)
    publicacion.estado = 'aprobado'
    publicacion.save()
    return redirect('moderar_publicaciones')


@login_required(login_url='/accounts/login/')
def rechazar_publicacion(request, pk):
    publicacion = get_object_or_404(PostAlumnos, pk=pk)
    publicacion.estado = 'rechazado'
    publicacion.save()
    return redirect('moderar_publicaciones')



@login_required(login_url='/accounts/login/')
def like_post(request, pk):
    post = get_object_or_404(PostAlumnos, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('publicaciones')



"""
@login_required(login_url='/accounts/login/')
def publicaciones(request):
    queryset = request.GET.get("buscar")
    
    if queryset:
        publicaciones = PostAlumnos.objects.filter(
            Q(nombre_post__icontains=queryset) |
            Q(descripcion_post__icontains=queryset)
        ).distinct()
        mensaje = None  # Reinicia el mensaje a None ya que hay resultados de búsqueda
    else:
        publicaciones = PostAlumnos.objects.all()  # Mostrar todas las publicaciones
        mensaje = "No se encontraron publicaciones con esa búsqueda."

    data = {
        "publicaciones": publicaciones,
        "mensaje": mensaje
    }

    return render(request, "publicaciones.html", data)
"""
@login_required(login_url='/accounts/login/')
def listarAlumnos(request):

    usuairos = Datos_Alumnos.objects.all()

    data={
        'usuarios': usuairos
    }
    return render(request, "mantenedor/listarAlumnos.html", data)



@login_required(login_url='/accounts/login/')
def eliminar_usuario(request, rut_Usuario):
    datos_usuarios = get_object_or_404(Datos_Alumnos, rut_Usuario=rut_Usuario)

    datos_usuarios.delete()
    messages.success(request, "El rut del usuario es : "+ rut_Usuario + " fue eliminado correctamente")

    return redirect(to="listarAlumnos")




@login_required(login_url='/accounts/login/')
def modificarAlumno(request, rut_Usuario):

    datos_usuario = get_object_or_404(Datos_Alumnos, rut_Usuario=rut_Usuario)

    data = {
        "formA": AlumnosForm(instance=datos_usuario)
    }

    if request.method == 'POST':
        formulario = AlumnosForm(data=request.POST, files=request.FILES, instance=datos_usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarAlumnos")
        else:
            data["mensaje"] = "Hubo un error"
            data["formA"] =  formulario


    return render(request, "mantenedor/modificarAlumno.html", data)


@login_required(login_url='/accounts/login/')
def listarModerador(request):

    moderador = Datos_Moderador.objects.all()

    data={
        'moderador': moderador
    }
    return render(request, "mantenedor/listarModerador.html", data)


@login_required(login_url='/accounts/login/')
def modificarModerador(request, rut_Moderador):

    datos_moderador = get_object_or_404(Datos_Moderador, rut_Moderador=rut_Moderador)

    data = {
        "formMo": ModeradorForm(instance=datos_moderador)
    }

    if request.method == 'POST':
        formulario = ModeradorForm(data=request.POST, files=request.FILES, instance=datos_moderador)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarModerador")
        else:
            data["mensaje"] = "Hubo un error"
            data["formMo"] =  formulario


    return render(request, "mantenedor/modificarModerador.html", data)

@login_required(login_url='/accounts/login/')
def eliminar_moderador(request, rut_Moderador):
    datos_moderador = get_object_or_404(Datos_Moderador, rut_Moderador=rut_Moderador)

    datos_moderador.delete()
    messages.success(request, "El rut del usuario es : "+ rut_Moderador + " fue eliminado correctamente")

    return redirect(to="listarModerador")


@login_required(login_url='/accounts/login/')
def crearEquipoView(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.idusercreador = request.user
            equipo.save()
            return redirect('homeAlumno')
    else:
        form = EquipoForm()
    return render(request, 'crearEquipo.html', {'form': form})


@login_required(login_url='/accounts/login/')
def chat_view(request):
    return render(request, 'chat.html')



@login_required(login_url='/accounts/login/')
def biblioteca(request):
    buscar = request.GET.get('buscar')
    if request.method == 'POST':
        form = LibrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('biblioteca')
    else:
        form = LibrosForm()
    
    # Obtener todos los libros de la base de datos
    libros = Libros.objects.all()

    if buscar:
        libros = libros.filter(titulo__icontains=buscar)

    context = {
        'formLibros': form,
        'libros': libros,
        'buscar': buscar,
    }

    return render(request, 'Biblioteca.html', context)




@login_required(login_url='/accounts/login/')
def modificarLibro(request, id):
    libro = get_object_or_404(Libros, id=id)
    if request.method == 'POST':
        form = LibrosForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('biblioteca')
    else:
        form = LibrosForm(instance=libro)
    return render(request, 'mantenedor/modificarLibro.html', {'formL': form, 'libro': libro})

@login_required(login_url='/accounts/login/')
def eliminarLibro(request, id):
    eliminarlibro = get_object_or_404(Libros, id=id)
    titulo = eliminarlibro.titulo  # Guarda el título del libro antes de eliminarlo
    eliminarlibro.delete()
    messages.success(request, f"El libro '{titulo}' fue eliminado correctamente.")
    return redirect('biblioteca')


@login_required(login_url='/accounts/login/')
def listarBiblioteca(request):
    buscar = request.GET.get('buscar')
    libros = Libros.objects.all()

    if buscar:
        libros = libros.filter(titulo__icontains=buscar)
    

    data = {'libros': libros}
    return render(request, 'mantenedor/listarBiblioteca.html', data)


@login_required(login_url='/accounts/login/')
def descargar_archivo(request, id):
    libro = get_object_or_404(Libros, id=id)
    archivo_path = libro.archivo_libro.path
    response = HttpResponse(open(archivo_path, 'rb'), content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename={libro.archivo_libro.name}'
    return response


def ver_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'ver_contactos.html', {'contactos': contactos})

