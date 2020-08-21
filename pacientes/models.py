from django.db import models
import datetime
from djrichtextfield.models import RichTextField
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    edad = models.IntegerField(default=0)
    sexo = models.CharField(max_length=20, null=True, blank=True, default='')
    ocupacion = models.CharField(max_length=50, null=True, blank=True, default='')
    calle = models.CharField(max_length=40, null=True, blank=True, default='')
    colonia = models.CharField(max_length=40, null=True, blank=True, default='')
    cp = models.CharField(max_length=8, null=True, blank=True, default='')
    celular = models.CharField(max_length=20, null=True, blank=True, default='')
    telefono = models.CharField(max_length=20, null=True, blank=True, default='')
    observaciones = models.TextField(null=True, blank=True, default='')
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_proxima_cita = models.DateTimeField(blank=True,null=True)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.nombre

class Consentimiento(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.PROTECT)
    documento = RichTextField(blank=True)
    obervaciones = models.TextField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=2, default='A')

class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente,on_delete=models.PROTECT)
    originario = models.CharField(max_length=50,blank=True,null=True)
    medico_particular = models.CharField(max_length=50,blank=True,null=True)
    telefono_medico = models.CharField(max_length=20,blank=True,null=True)
    motivo_cita = models.CharField(max_length=128,blank=True,null=True)
    enfermedad_ultimo_anos = models.CharField(max_length=100,blank=True,null=True)
    enfermedad_grave = models.CharField(max_length=100, blank=True, null=True)
    cirugias = models.CharField(max_length=100,blank=True,null=True)
    traumatismos_secuelas =models.CharField(max_length=100,blank=True,null=True)
    transfusiones = models.CharField(max_length=100,blank=True,null=True)
    hemorragias = models.CharField(max_length=100,blank=True,null=True)
    donador_sangre = models.CharField(max_length=100,blank=True,null=True)
    accidentes_tratamientos=models.CharField(max_length=100,blank=True,null=True)
    tratamiento_medico_padecimientos = models.CharField(max_length=100,blank=True,null=True)
    toma_medicamento =models.CharField(max_length=200,blank=True,null=True)
    enfermedades=models.CharField(max_length=200,blank=True,null=True)
    familiar_enfermedad  = models.CharField(max_length=100,blank=True,null=True)
    actualmente_algun_familiar_enfermo=models.CharField(max_length=100,blank=True,null=True)
    actualmente_estaenfermo =models.CharField(max_length=100,blank=True,null=True)
    embarazada =models.CharField(max_length=100,blank=True,null=True)
    higiene = models.CharField(max_length=1,blank=True,null=True) # B=Buena R=Regular S=Supervisar
    numero_cepillados = models.CharField(max_length=30,blank=True,null=True)
    alimentacion = models.CharField(max_length=1,blank=True,null=True) # B=Buena R=Regualar B=Buena
    integrantes_casa = models.CharField(max_length=20,blank=True,null=True)
    practica_deportes = models.CharField(max_length=20,blank=True,null=True)
    habito_adiccion = models.CharField(max_length=100,blank=True,null=True)
    temperatura =models.CharField(max_length=100,blank=True,null=True)
    presion =models.CharField(max_length=100,blank=True,null=True)
    pulso = models.CharField(max_length=100,blank=True,null=True)
    tratamientos_odontologicos = models.CharField(max_length=100,blank=True,null=True)
    alergico_anestesia = models.CharField(max_length=100,blank=True,null=True)
    experiencia_tratamientos =models.CharField(max_length=100,blank=True,null=True)
    articulacion_temporo = models.CharField(max_length=100,blank=True,null=True)
    dolor_articulacion = models.BooleanField(default=False)
    chasquidos = models.BooleanField(default=False)
    limitacion_apertura = models.BooleanField(default=False)
    limitacion_moviientos = models.BooleanField(default=False)
    bruxismo= models.BooleanField(default=False)
    obervaciones = models.TextField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=2, default='A')



    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.nombre