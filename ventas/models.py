from django.db import models
from inventarios.models import *
from pacientes.models import *
from datetime import datetime

# Create your models here

class DetPresupuesto(models.Model):
    id = models.AutoField(primary_key=True)
    id_articulo = models.ForeignKey(Articulos, on_delete=models.PROTECT)
    obervacion = models.CharField(null=False, blank=False, max_length=120)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']

class Presupuesto(models.Model):  # Ford Company, GMC
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    observacion = models.TextField(max_length=256)
    fecha_presupuesto = models.DateTimeField(auto_now_add=datetime.now(), blank=False, null=False) # + 30
    fecha_vence = models.DateTimeField(auto_now_add=datetime.now(), blank=False, null=False) # 30 días
    total = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=2)
    iva = models.DecimalField(blank=False, null=False, max_digits=3, decimal_places=2)
    id_det_presupuesto = models.ForeignKey(DetPresupuesto,on_delete=models.PROTECT)
    creado = models.DateTimeField(auto_created=datetime.now())
    actualizado = models.DateTimeField(auto_now_add=datetime.now())
    estatus = models.CharField(max_length=2)

    def _str__(self):
        return self.provedoor

    class Meta:
        ordering = ['id']


class DetVentas(models.Model):
    id = models.AutoField(primary_key=True)
    id_articulo = models.ForeignKey(Articulos, on_delete=models.PROTECT)
    obervacion = models.CharField(null=False, blank=False, max_length=120)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']


class Ventas(models.Model):  # Ford Company, GMC
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    observacion = models.TextField(max_length=256)
    fecha_venta = models.DateTimeField(auto_now_add=datetime.now(), blank=False, null=False)
    total = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=2)
    iva = models.DecimalField(blank=False, null=False, max_digits=3, decimal_places=2)
    id_det_ventas = models.ForeignKey(DetPresupuesto, on_delete=models.PROTECT)
    creado = models.DateTimeField(auto_created=datetime.now())
    actualizado = models.DateTimeField(auto_now_add=datetime.now())
    estatus = models.CharField(max_length=2)

    def _str__(self):
        return self.provedoor

    class Meta:
        ordering = ['id']



