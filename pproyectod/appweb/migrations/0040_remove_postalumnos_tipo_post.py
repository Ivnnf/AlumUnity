# Generated by Django 5.0.3 on 2024-06-03 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0039_postalumnos_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postalumnos',
            name='tipo_post',
        ),
    ]
