from django.db import models

# Create your models here.

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=80)
    estatus = models.CharField(max_length=1, default='A')
    fecha = models.DateTimeField(auto_now_add=True)


class Doctores(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    especialidad = models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=80)
    telefono_partucular = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=1, default='A')
