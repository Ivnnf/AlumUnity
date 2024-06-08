from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils import timezone
# Create your models here.



from django.db import models

class Contacto(models.Model):
    TIPOS_CONTACTO = [
        ("Consulta", "Consulta"),
        ("Sugerencia", "Sugerencia"),
        ("Problemas con tu cuenta", "Problemas con tu cuenta")
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('revisado', 'Revisado')
    ]

    nombre_contacto = models.CharField(max_length=100)
    correo_contacto = models.EmailField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    mensaje_contacto = models.TextField()
    tipos_contacto = models.CharField(max_length=50, choices=TIPOS_CONTACTO, default='Consulta')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.nombre_contacto} - {self.correo_contacto}"


class Libros(models.Model):
    CATEGORIAS = [
        ("tecnología", 'tecnología'),
        ("informática", 'informática'),
        ("Científicos", 'Científicos'),
        ("Matemáticas", 'Matemáticas'),
        ("Medicina", 'Medicina'),
        ("De referencia o consulta", 'De referencia o consulta'),
        ("Biografías", 'Biografías'),
        ("Literatura y lingüísticos", 'Literatura y lingüísticos'),
        # Agrega más categorías si es necesario
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    fecha_publicacion = models.DateField()
    archivo_libro = models.FileField(upload_to="libros", null=True, blank=True)
    portada = models.ImageField(upload_to="portadas", null=True, blank=True)

    def __str__(self):
        return self.titulo






class Datos_Moderador(models.Model):
    nombre_Moderador = models.CharField(max_length=50)
    apellido_Moderador = models.CharField(max_length=50)
    rut_Moderador = models.CharField(max_length=12)
    telefono_Moderador = models.CharField(max_length=20, default='+569 ')
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    confirmar_password = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.nombre_Moderador




class PostAlumnos(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    )

    nombre_post = models.CharField(max_length=50)
    descripcion_post = models.TextField(max_length=200)
    imagen_post = models.ImageField(upload_to="AlumnosP", null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return self.nombre_post

    def total_likes(self):
        return self.likes.count()

"""
t_post = [

    [ "Grupo Estudio", "Grupo Estudio"],
    [ "Grupo Equipo", "Grupo Equipo"],
    [ "Grupo Ocio", "Grupo Ocio"],

]

class PostAlumnos(models.Model):
    nombre_post = models.CharField(max_length=50)
    descripcion_post = models.TextField(max_length=200)
    tipo_post = models.IntegerField(choices=t_post)
    imagen_post = models.ImageField(upload_to="AlumnosP", null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.nombre_post

    def total_likes(self):
        return self.likes.count()
"""
carreras = [

    ["Analista Programador Computacional", "Analista Programador Computacional"],
    ["Contabilidad Tributaria", "Contabilidad Tributaria"],
    ["Administración de Empresas", "Administración de Empresas"],
    ["Desarrollo de Aplicaciones", "Desarrollo de Aplicaciones"],
    ["ingeniería en Desarrollo de Software", "ingeniería en Desarrollo de Software"],
    

]

class Datos_Alumnos(models.Model):
    nombre_Usuario = models.CharField(max_length=50)
    apellido_Usuario = models.CharField(max_length=50)
    rut_Usuario = models.CharField(max_length=12)
    telefono_Usuario = models.CharField(max_length=20, default='+569 ')
    carrera_Usuario = models.CharField(max_length=100, choices=carreras, default='')
    semestre_Usuario = models.CharField(max_length=12,default='')
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    confirmar_password = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.nombre_Usuario
    

class Status(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fechacreacion = models.DateTimeField(default=timezone.now)
    idusercreador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_equipos/', blank=True, null=True)
    idStatus = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    idTipoEquipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombreEquipo

class PreferenciaEquipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    preferencia = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.equipo.nombreEquipo} - {self.preferencia}: {self.valor}"



    


class Comentario(models.Model):
    publicacion = models.ForeignKey(PostAlumnos, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario por {self.autor.username} en {self.publicacion.nombre_post}'

