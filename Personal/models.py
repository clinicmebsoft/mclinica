from datetime import datetime

from django.db import models

# Create your models here.

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=80)
    estatus = models.CharField(max_length=1, default='A')
    fecha = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return self.especialidad

class Doctores(models.Model):
    nombre = models.CharField(max_length=30,default='')
    apellidos = models.CharField(max_length=50,default='')
    correo = models.CharField(max_length=100,default='')
    fecha_nat = models.DateTimeField(default=datetime.now)
    sexo = models.CharField(max_length=12,default='')
    especialidad = models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    cp = models.CharField(max_length=6,default='')
    callenum =models.CharField(max_length=50,default='')
    colonia =models.CharField(max_length=40,default='')
    ciudad =models.CharField(max_length=40,default='')
    estado =models.CharField(max_length=40,default='')
    pais =models.CharField(max_length=20,default='')
    telefono_particular = models.CharField(max_length=20,default='')
    celular = models.CharField(max_length=20,default='')
    fecha = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=1, default='A')
    observaciones =models.CharField(max_length=255,default='')

    def _str__(self):
        return self.id