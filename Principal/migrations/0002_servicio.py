# Generated by Django 5.0.6 on 2024-07-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
    ]
