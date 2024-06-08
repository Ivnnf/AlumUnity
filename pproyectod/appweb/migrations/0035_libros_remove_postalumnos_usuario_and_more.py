# Generated by Django 5.0.3 on 2024-05-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0034_merge_20240518_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('categoria', models.IntegerField(choices=[('tecnología', 'tecnología'), ('informática', 'informática'), ('Científicos', 'Científicos'), ('Matemáticas', 'Matemáticas'), ('Medicina', 'Medicina'), ('De referencia o consulta', 'De referencia o consulta'), ('Biografías', 'Biografías'), ('Literatura y lingüísticos', 'Literatura y lingüísticos')])),
                ('fecha_publicacion', models.DateField()),
                ('archivo_libro', models.FileField(blank=True, null=True, upload_to='libros')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas')),
            ],
        ),
        migrations.RemoveField(
            model_name='postalumnos',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='datos_alumnos',
            name='correo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='postalumnos',
            name='imagen_post',
            field=models.ImageField(null=True, upload_to='AlumnosP'),
        ),
        migrations.AlterField(
            model_name='postalumnos',
            name='tipo_post',
            field=models.IntegerField(choices=[('Grupo Estudio', 'Grupo Estudio'), ('Grupo Equipo', 'Grupo Equipo'), ('Grupo Ocio', 'Grupo Ocio')]),
        ),
    ]
