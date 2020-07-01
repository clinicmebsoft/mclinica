from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from pacientes.models import Paciente

from django.core import serializers
import json


# Create your views here.
def index(request):  # usuario no activo mandar al login
    return render(request, "pacientes/paciente.html")


def pacientes(request):
    return render(request, "pacientes/paciente.html")


def listapacientes(request):
    return render(request, "pacientes/listapacientes.html")

def historiaclinica(request):
    return render(request, "pacientes/historiaclinica.html")


def ajax_buscapacientes(request):
    busca = request.GET.get('empieza')
    if request.is_ajax():
        # print(busca)
        pacientes = Paciente.objects.filter(nombre__icontains=busca)
        paciente = []
        for p in pacientes:
            p_json = {}

            p_json['id'] = p.id
            p_json['nombre'] = p.nombre
            p_json['apellidos'] = p.apellidos
            paciente.append(p_json)
        # data_json = json.dumps(paciente)
    else:
        data_json = "Busqueda falló"
    mimetype = 'application/json'

    return JsonResponse({
        'respuesta': {
            'paciente': paciente
        }
    })


def ajax_guardapaciente(request):
    resp = ""
    paciente = Paciente()
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body)
        # print(json_data)

        nombre =  json_data['nombre']
        apellidos = json_data['apellidos']
        correo = json_data['correo']
        if Paciente.objects.filter(nombre=nombre, apellidos=apellidos, correo=correo):
            resp = "Ya existe un paciente con ese nombre y correo"
        else:
            # print('nombre' + str(nombre))
            paciente.nombre = str.upper(nombre)
            paciente.apellidos = str.upper(apellidos)
            paciente.correo = correo
            paciente.fecha_nacimiento = json_data['fechanacimiento']
            paciente.edad = int(json_data['edad'])

            paciente.celular = json_data['celular']
            paciente.save()
            resp = "Registro Guardado..."

    else:
        resp = "Error al guardar registro"

    return JsonResponse({
        'respuesta': {
            'mensaje': resp,
        }
    })

def ax_CargaTpacientes(request):
    pacientes = Paciente.objects.exclude(estatus='C').all().values('id','nombre','apellidos','calle','telefono','celular','correo')
    data = json.dumps({"data": list(pacientes)})
    return HttpResponse(data)


def ajax_obtenDatosPacienteCitas(request):
    id = request.GET.get('id')
    if request.is_ajax():
        try:
            paciente = Paciente.objects.filter(id=id)
            data = serializers.serialize('json', paciente,
                                         fields=('nombre', 'apellidos', 'correo', 'telefono', 'celular'))
            return HttpResponse(data, content_type='application/json')
        except:
            return HttpResponse("Error al intentar recuperar datos")
