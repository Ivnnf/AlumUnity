# Generated by Django 4.2.1 on 2024-03-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_datos_alumnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_alumnos',
            name='telefono_Usuario',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipos_contacto',
            field=models.IntegerField(choices=[[0, 'Consulta'], [1, 'Sugerencia'], [2, 'Problemas con tu cuenta']]),
        ),
    ]
