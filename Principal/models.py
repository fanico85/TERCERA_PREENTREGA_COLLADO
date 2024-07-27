from django.db import models

# Create your models here.

class Usuario(models.Model):
    us_nombre = models.CharField(max_length=30)
    us_contrasenia = models.CharField(max_length=20)
    us_rol = models.CharField(max_length=20)

class Servicio(models.Model):
    ser_nombre = models.CharField(max_length=50)
    ser_descripcion = models.CharField(max_length=100, default="descripcion")
    ser_duracion = models.IntegerField(default=1)

class Gasto(models.Model):
    gas_nombre = models.CharField(max_length=50)
    gas_descripcion = models.CharField(max_length=100)
    gas_monto = models.DecimalField(max_digits=10,decimal_places=2)
    gas_fecha = models.DateField()
