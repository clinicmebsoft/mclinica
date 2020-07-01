from pacientes.models import Paciente


def buscaPaciente(nombre,apellidos,corre):
    pac=0
    try:
        paciente = Paciente.objects.get(nombre=nombre,apellidos=apellidos,correo=corre)
    except Paciente.DoesNotExist:
        pass
    else:
        pac = paciente.id

    return pac