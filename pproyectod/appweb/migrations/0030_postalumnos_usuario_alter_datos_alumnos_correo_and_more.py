# Generated by Django 5.0.3 on 2024-05-18 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0029_alter_contacto_tipos_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='postalumnos',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appweb.datos_alumnos'),
        ),
        migrations.AlterField(
            model_name='datos_alumnos',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='postalumnos',
            name='imagen_post',
            field=models.ImageField(blank=True, null=True, upload_to='AlumnosP'),
        ),
    ]
