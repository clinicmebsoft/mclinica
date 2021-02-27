
from django.contrib import admin
from pacientes.models import *
from inventarios.models import *
# Register your models here.


admin.site.register(Paciente)
admin.site.register(HistoriaClinica)
admin.site.register(Articulos)
admin.site.register(Impuestos)
admin.site.register(Proveedores)




