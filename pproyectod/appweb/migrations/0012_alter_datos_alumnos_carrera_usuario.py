# Generated by Django 5.0.3 on 2024-03-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0011_datos_alumnos_semestre_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_alumnos',
            name='carrera_Usuario',
            field=models.IntegerField(choices=[(0, 'Analista Programador Computacional'), (1, 'Contabilidad Tributaria'), (2, 'Administración de Empresas'), (3, 'Desarrollo de Aplicaciones'), (4, 'ingeniería en Desarrollo de Software')], default='+569 '),
        ),
    ]
