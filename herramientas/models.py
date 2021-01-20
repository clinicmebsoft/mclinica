from django.db import models

# Create your models here.
from django.db.models import Model

class Codigo_postal(models.Model):
    d_codigo = models.CharField(null=True,blank=True, max_length=8)
    d_asenta = models.CharField(null=True,blank=True, max_length=100)
    d_tipo_asenta = models.CharField(null=True,blank=True, max_length=100)
    d_mnpio = models.CharField(null=True,blank=True, max_length=80)
    d_estado = models.CharField(null=True,blank=True, max_length=50)
    d_ciudad = models.CharField(null=True,blank=True, max_length=50)
    d_cp = models.CharField(null=True,blank=True, max_length=8)
    c_estado = models.CharField(null=True,blank=True, max_length=8)
    c_oficina = models.CharField(null=True,blank=True, max_length=8)
    c_cp = models.CharField(null=True,blank=True, max_length=8)
    c_tipo_asenta = models.CharField(null=True,blank=True, max_length=8)
    c_mnpio = models.CharField(null=True,blank=True, max_length=8)
    id_asenta_cpcons = models.CharField(null=True,blank=True, max_length=8)
    d_zona = models.CharField(null=True,blank=True, max_length=100)
    c_cve_ciudad = models.CharField(null=True,blank=True, max_length=8)

    def _str__(self):
        return self.d_asenta

    class Meta:
        ordering = ['d_codigo']