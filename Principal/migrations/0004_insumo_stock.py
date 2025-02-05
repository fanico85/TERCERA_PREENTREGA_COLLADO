# Generated by Django 5.0.6 on 2024-07-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0003_gasto_remove_servicio_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_codigo', models.CharField(max_length=20)),
                ('ins_nombre', models.CharField(max_length=50)),
                ('ins_marca', models.CharField(max_length=50)),
                ('ins_stock', models.IntegerField()),
                ('ins_unidad_medida', models.CharField(max_length=20)),
                ('ins_contenido', models.IntegerField()),
                ('ins_descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_actual', models.IntegerField()),
                ('st_minimo', models.IntegerField()),
                ('st_maximo', models.IntegerField(null=True)),
                ('st_fecha_actualizacion', models.DateTimeField(null=True)),
            ],
        ),
    ]
