from django.db import models

# Create your models here.
class Proveedores(models.Model):
    id = models.AutoField(primary_key=True)
    razon_social=models.CharField(max_length=100)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    cp= models.CharField(max_length=8, null=True, blank=True, default='')
    estado=models.CharField(max_length=40, null=True, blank=True, default='')
    municipio=models.CharField(max_length=40, null=True, blank=True, default='')
    colonia = models.CharField(max_length=40, null=True, blank=True, default='')
    calle = models.CharField(max_length=40, null=True, blank=True, default='')
    web = models.CharField(max_length=100, null=True, blank=True, default='')
    celular = models.CharField(max_length=20, null=True, blank=True, default='')
    telefono = models.CharField(max_length=20, null=True, blank=True, default='')
    observaciones = models.TextField(null=True, blank=True, default='')
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.nombre