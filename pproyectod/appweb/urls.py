
from .views import *
from . import views
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include
# project/urls.py
from django.contrib.auth import views as auth_views




urlpatterns = [


    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('home/',home, name="home" ),
    path('baseContacto/', baseContacto , name="baseContacto" ),
    path('homeAdmin/', homeAdmin ,name="homeAdmin"),
    
    path('contacto/', contacto, name='contacto'),
    path('ver-contactos/', views.ver_contactos, name='ver_contactos'),
    path('gestionar_contactos/', views.gestionar_contactos, name='gestionar_contactos'),

    path('login_usuario/' , login_usuario , name="login_usuario"),
    path('registroUsuarios/',registroUsuarios, name="registroUsuarios"),
    path('homeAlumno/', homeAlumno ,name="homeAlumno"),
    path('registroUsuariosAdmin/', registroUsuariosAdmin ,name="registroUsuariosAdmin"),
    path('homeModerador/', homeModerador , name="homeModerador"),
    path('postAlumno/', postAlumnos , name="postAlumno"),

    path('comentario/eliminar/<int:pk>/', views.eliminar_comentario, name='eliminar_comentario'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('like/<int:pk>/', like_post, name="like_post"),
    path('moderar/', moderar_publicaciones, name="moderar_publicaciones"),
    path('aprobar/<int:pk>/', aprobar_publicacion, name="aprobar_publicacion"),
    path('rechazar/<int:pk>/', rechazar_publicacion, name="rechazar_publicacion"),



    path('biblioteca/', biblioteca , name="biblioteca" ),
    path('modificarLibro/<int:id>/', modificarLibro , name="modificarLibro" ),
    path('eliminarLibro/<int:id>/', eliminarLibro, name='eliminarLibro'),
    path('descargar_archivo/<int:id>/', views.descargar_archivo, name='descargar_archivo'),

    path('listarBiblioteca/', listarBiblioteca, name='listarBiblioteca'),

    path('listarAlumnos/', listarAlumnos, name="listarAlumnos"),
    path('modificarAlumno/<rut_Usuario>',modificarAlumno,name='modificarAlumno'),
    path('eliminar_usuario/<rut_Usuario>/', eliminar_usuario, name="eliminar_usuario"),
    
    path('listarModerador/', listarModerador, name="listarModerador"),
    path('modificarModerador/<rut_Moderador>',modificarModerador,name='modificarModerador'),
    path('eliminar_moderador/<rut_Moderador>/', eliminar_moderador, name="eliminar_moderador"),
    
    path('crearEquipo/', crearEquipoView, name='crearEquipo'),
    path('chat/', views.chat_view, name='chat'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration2/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration2/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration2/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration2/password_reset_complete.html'), name='password_reset_complete'),
]
