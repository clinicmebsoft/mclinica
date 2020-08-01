from django.db import models
from datetime import datetime
from proveedores.models import Proveedores

class Categorias(models.Model):  # Ejemplos Insumos Odontología, Insumos , Medicamentos, etc
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=60)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.id

    class Meta:
        ordering = ['id']

class Unidades(models.Model):  # kilos, gramos, 24 , 100, etc
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=60)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']


class Marcas(models.Model):  # Ford, Nissan, etc
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=60)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']


class Fabricantes(models.Model):  # Ford Company, GMC
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=60)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']


class Impuestos(models.Model):  # Ford Company, GMC
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=30)
    porcentaje = models.FloatField(null=True,max_length=4, blank=True)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']





class Compuesto(models.Model):
    id = models.AutoField(primary_key=True)
    id_articulo = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']


class Articulos(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(null=False, blank=False, max_length=10)  # S=servicio P=Producto
    clave = models.CharField(null=False, blank=False, max_length=10,default='0')
    descripcion = models.CharField(null=False, blank=False, max_length=120)
    codigobarras = models.CharField(max_length=30)
    id_categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    id_unidades = models.ForeignKey(Unidades, on_delete=models.PROTECT)
    id_marcas = models.ForeignKey(Marcas, on_delete=models.PROTECT)
    id_fabricantes = models.ForeignKey(Fabricantes, on_delete=models.PROTECT)
    precioventa = models.FloatField(max_length=14)
    costo = models.FloatField(max_length=14)
    stock_min = models.IntegerField(default=0)
    stock_max = models.IntegerField(default=0)
    reorden = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    id_impuestos = models.ForeignKey(Impuestos, on_delete=models.PROTECT)
    id_proveedores = models.ForeignKey(Proveedores, on_delete=models.PROTECT)
    compuesto = models.BooleanField(default=False)  # Si compuesto TRUE afectar inventarios de los artículos de compuesto
    id_compuesto = models.ForeignKey(Compuesto, on_delete=models.PROTECT,default=0)
    creado = models.DateTimeField(auto_created=True, blank=True, null=True)
    actualizado = models.DateTimeField(auto_now_add=datetime.now(), blank=True, null=True)
    estatus = models.CharField(max_length=2, default='A')

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']
