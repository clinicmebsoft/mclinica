from django.db import models

from pacientes.models import Paciente

'''

1) Remove the migration history for each app.

python manage.py migrate --fake core zero

2) Blow away any migration files in the entire project within which the app(s) reside.

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

3) Make migrations

python manage.py makemigrations

4) Apply the migrations, faking initial because the database already exists and we just want the changes:

python manage.py migrate --fake-initial

'''

# python manage.py makemigrations
# python manage.py migrate

# Create your models here.

class Cita(models.Model):  # las citas de guardan con relacio paciente-cita si no exite el paciente
    # se guardan sólo nombre apellidos correo telefono
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    motivo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateField(auto_now_add=True)
    atendio = models.CharField(max_length=5)
    observacion = models.TextField(max_length=512)
    estatus = models.CharField(max_length=2)

    def _str__(self):
        return self.fecha

    class Meta:
        ordering = ['id']
