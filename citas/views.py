from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from pacientes.models import Paciente
from citas.models import Cita
from django.core import serializers
from pacientes.functpacientes import buscaPaciente

import json


# Create your views here.
def index(request):
    return render(request, "citas/cita.html")


# http://www.lalicode.com/post/5/

def guardacitas(request):
    resp = ""

    paciente = Paciente()
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body)

        pacid = buscaPaciente(json_data['nombre'],json_data['apellidos'],json_data["correo"])
        cita =Cita.objects.filter(id_paciente=pacid, fecha=json_data["fecha"]).count()
        if cita>0:
            resp = "Ya existe una cita igual..."
        else:
            if pacid < 1:
                paciente.nombre = json_data['nombre']
                paciente.apellidos = json_data['apellidos']
                paciente.correo = json_data["correo"]
                paciente.celular = json_data['celular']
                paciente.estatus = "IP"  # paciente con información parcial cuando se atienda en la cita se hace el compelemento
                paciente.telefono = json_data['telefono']
                paciente.observaciones = json_data["motivo"]
                paciente.save()

            pacid = buscaPaciente(json_data['nombre'],json_data['apellidos'],json_data["correo"])
            cita = Cita()
            cita.nombre = json_data['nombre']
            cita.apellidos = json_data['apellidos']
            cita.telefono = json_data['telefono']
            cita.celular = json_data['celular']
            cita.correo = json_data["correo"]
            cita.fecha = json_data["fecha"]
            cita.hora = json_data["hora"]
            cita.motivo = json_data["motivo"]
            cita.id_paciente = Paciente.objects.get(id = pacid)
            cita.save()
            resp = "La cita ha sido Guardada..."


    else:
        resp = "Error al intentar guardar la cita "

    return JsonResponse({
        'respuesta': {
            'mensaje': resp,
        }
    })


def buscarcitas(request):
    return render(request, "citas/buscar.html")


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


def ajax_BuscaPacientes(request):
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
