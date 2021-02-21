from django import forms
from django.contrib.auth.models import User
from django.db import models
import datetime

from django.db.models import CharField
from django.forms import ModelForm
from djrichtextfield.models import RichTextField

# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
from personal.models import Doctores
from inventarios.models import Articulos


class Paciente(models.Model):
    SEXO = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('No definido', 'No definido')
    )
    doctor = models.ForeignKey(Doctores,models.PROTECT)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    edad = models.IntegerField(default=0)
    sexo = models.CharField(max_length=12, null=True, blank=True, default='No definido', verbose_name='sexo',
                            choices=SEXO)
    ocupacion = models.CharField(max_length=50, null=True, blank=True, default='')
    calle = models.CharField(max_length=40, null=True, blank=True, default='')
    colonia = models.CharField(max_length=40, null=True, blank=True, default='')
    cp = models.CharField(max_length=8, null=True, blank=True, default='')
    celular = models.CharField(max_length=20, null=True, blank=True, default='')
    ciudad = models.CharField(max_length=30, null=True, blank=True, default='')
    telefono = models.CharField(max_length=20, null=True, blank=True, default='')
    estado = models.CharField(max_length=30, null=True, default='Jalisco')
    pais = models.CharField(max_length=30, null=True, default='México')
    observaciones = models.TextField(null=True, blank=True, default='')
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_proxima_cita = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.nombre + " " + self.apellidos


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        SEXO = (
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No definido', 'No definido')
        )  # estos campos son importantes definirlos para que los procese
        fields = ['nombre', 'apellidos', 'correo', 'fecha_nacimiento', 'edad', 'sexo', 'ocupacion',
                  'calle', 'colonia', 'cp', 'celular', 'telefono', 'estado', 'pais', 'observaciones']


class Consentimiento(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    documento = RichTextField(blank=True)
    obervaciones = models.TextField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=2, default='A')


class HistoriaClinica(models.Model):
    HIGIENE = (
        ("Buena", "Buena"),
        ("Supervisar", "Supervisar"),
        ("Regular", "Regular"),
        ("Pendiente", "Pendiente")
    )
    ALIMENTACION = (
        ("Buena", "Buena"),
        ("Mala", "Mala"),
        ("Regular", "Regular"),
        ("Pendiente", "Pendiente")
    )
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    originario = models.CharField(max_length=50, blank=True, default='')
    medico_particular = models.CharField(max_length=50, blank=True, default='')
    telefono_medico = models.CharField(max_length=20, blank=True, default='')
    motivo_cita = models.CharField(max_length=128, blank=True, default='')
    enfermedad_ultimo_anos = models.CharField(max_length=100, blank=True, default='No')
    enfermedad_grave = models.CharField(max_length=100, blank=True, default='No')
    cirugias = models.CharField(max_length=100, blank=True, default='No')
    traumatismos_secuelas = models.CharField(max_length=100, blank=True, default='No')
    transfusiones = models.CharField(max_length=100, blank=True, default='No')
    hemorragias = models.CharField(max_length=100, blank=True, default='No')
    donador_sangre = models.CharField(max_length=100, blank=True, default='No')
    accidentes_tratamientos = models.CharField(max_length=100, blank=True, default='No')
    tratamiento_medico_padecimientos = models.CharField(max_length=100, blank=True, default='No')
    toma_medicamento = models.CharField(max_length=200, blank=True, default='No')
    enfermedades = models.CharField(max_length=200, blank=True, default='No')
    familiar_enfermedad = models.CharField(max_length=100, blank=True, default='No')
    actualmente_algun_familiar_enfermo = models.CharField(max_length=100, blank=True, default='No')
    actualmente_estaenfermo = models.CharField(max_length=100, blank=True, default='No')
    embarazada = models.CharField(max_length=100, blank=True, default='No')
    higiene = models.CharField(max_length=10, blank=True, choices=HIGIENE,
                               default='Buena')  # B=Buena R=Regular S=Supervisar
    numero_cepillados = models.IntegerField(blank=True, default=0)
    alimentacion = models.CharField(max_length=10, blank=True, choices=ALIMENTACION,
                                    default='Buena')  # B=Buena R=Regualar B=Buena
    integrantes_casa = models.IntegerField(blank=True, default=0)
    practica_deportes = models.CharField(max_length=20, blank=True, default='No')
    habito_adiccion = models.CharField(max_length=100, blank=True, default='No')
    temperatura = models.IntegerField(blank=True, default=0)
    presion = models.CharField(max_length=10, blank=True, default=0)
    pulso = models.IntegerField(blank=True, default=0)
    tratamientos_odontologicos = models.CharField(max_length=100, blank=True, default='No')
    alergico_anestesia = models.CharField(max_length=100, blank=True, default='No')
    experiencia_tratamientos = models.CharField(max_length=100, blank=True, default='No')
    articulacion_temporo = models.CharField(max_length=100, blank=True, default='No')

    dolor_articulacion = models.BooleanField(default=False, null=True)
    chasquidos = models.BooleanField(default=False, null=True)
    limitacion_apertura = models.BooleanField(default=False, null=True)
    limitacion_movimientos = models.BooleanField(default=False, null=True)
    bruxismo = models.BooleanField(default=False, null=True)

    obervaciones = models.TextField(blank=True, default='')
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=2, default='A')

    def _str__(self):
        return self.nombre


class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        HIGIENE = (
            ("Buena", "Buena"),
            ("Supervisar", "Supervisar"),
            ("Regular", "Regular"),
            ("Pendiente", "Pendiente")
        )
        ALIMENTACION = (
            ("Buena", "Buena"),
            ("Mala", "Mala"),
            ("Regular", "Regular"),
            ("Pendiente", "Pendiente")
        )
        fields = ['id_paciente', 'originario', 'medico_particular', 'telefono_medico', 'motivo_cita',
                  'enfermedad_ultimo_anos',
                  'enfermedad_grave', 'cirugias', 'traumatismos_secuelas', 'transfusiones', 'hemorragias',
                  'donador_sangre', 'accidentes_tratamientos', 'tratamiento_medico_padecimientos', 'toma_medicamento',
                  'enfermedades', 'familiar_enfermedad', 'actualmente_algun_familiar_enfermo',
                  'actualmente_estaenfermo',
                  'embarazada', 'higiene', 'numero_cepillados', 'alimentacion', 'integrantes_casa', 'practica_deportes',
                  'habito_adiccion', 'temperatura', 'presion', 'pulso', 'tratamientos_odontologicos',
                  'alergico_anestesia',
                  'experiencia_tratamientos', 'articulacion_temporo', 'dolor_articulacion', 'chasquidos',
                  'limitacion_apertura',
                  'limitacion_movimientos', 'bruxismo', 'obervaciones'
                  ]





class ListaTratamientos(models.Model):
    tratamiento = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)


class Tratamientos(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)


class PresuPaciente(models.Model):
    id_doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='id_paciente')
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    vence = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=30))
    obervaciones = models.TextField(blank=True, default='')
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estatus = models.CharField(max_length=1, default='A')


class PresuPacienteDetalle(models.Model):
    id_presupuesto = models.ForeignKey(PresuPaciente, on_delete=models.CASCADE)
    id_tratamiento = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=0)


class Odontograma(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    pieza = models.IntegerField(blank=True, default=0)
    caras = models.CharField(max_length=5)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estatus = models.CharField(max_length=1, default='A')
