from django.db import migrations

def create_initial_data(apps, schema_editor):
    Status = apps.get_model('appweb', 'Status')
    TipoEquipo = apps.get_model('appweb', 'TipoEquipo')
    
    Status.objects.create(nombre='Activo')
    Status.objects.create(nombre='Inactivo')
    
    TipoEquipo.objects.create(nombre='Tipo 1')
    TipoEquipo.objects.create(nombre='Tipo 2')

class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0030_status_tipoequipo_equipo_preferenciaequipo'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
