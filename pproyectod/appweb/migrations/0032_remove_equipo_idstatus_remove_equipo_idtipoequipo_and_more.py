# Generated by Django 5.0.3 on 2024-05-15 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0031_populate_initial_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='idstatus',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='idtipoEquipo',
        ),
        migrations.RemoveField(
            model_name='status',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='tipoequipo',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='tipoequipo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='equipo',
            name='idStatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appweb.status'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='idTipoEquipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appweb.tipoequipo'),
        ),
    ]
