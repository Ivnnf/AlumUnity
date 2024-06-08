# Generated by Django 5.0.3 on 2024-06-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0040_remove_postalumnos_tipo_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('revisado', 'Revisado')], default='pendiente', max_length=10),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='correo_contacto',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipos_contacto',
            field=models.CharField(choices=[('Consulta', 'Consulta'), ('Sugerencia', 'Sugerencia'), ('Problemas con tu cuenta', 'Problemas con tu cuenta')], default='Consulta', max_length=50),
        ),
    ]
