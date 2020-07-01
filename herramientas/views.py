
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json


# Create your views here.
from django.views.decorators.csrf import csrf_protect

from citas.models import Cita
from herramientas.models import Codigo_postal
from mebClinic.settings import BASE_DIR


def agenda(request):
    return render(request, "herramientas/agenda.html")


def administracion(request):
    return render(request, "extras/administracion.html")


def ax_agenda(request):
    citas = Cita.objects.filter(estatus='').values('id_paciente', 'id_paciente__nombre', 'fecha', 'hora')
    cita_dic = []
    for cit in citas:
        dict = {}
        # for campos in cit:
        dict['id'] = cit['id_paciente']
        dict['nombre'] = cit['id_paciente__nombre']
        dict['fecha'] = str(cit['fecha']) + 'T' + str(cit['hora'])
        cita_dic.append(dict)
    return HttpResponse(json.dumps(cita_dic), content_type="application/json")


@csrf_protect
def ax_citas(request):
    # citas = Cita.objects.exclude(estatus='C').all().values('id_paciente', 'nombre','fecha', 'hora')
    citas = Cita.objects.select_related('paciente')
    for r in citas:
        print(r.nombre)
    data = [
        {
            'id': '1',
            'nombre': 'event1',
            'fecha': '2010-01-01'
        },
        {
            'id': '2',
            'nombre': 'event2',
            'fecha': '2010-01-05'

        }
    ]
    return JsonResponse(data, safe=False)


def ax_buscar_cp(request):
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body)
        cp = json_data['cp']
        cod_postal = Codigo_postal.objects.filter(d_codigo=cp).values('d_codigo','d_asenta','d_mnpio','d_estado','d_ciudad')

        data = json.dumps({"data_cp": list(cod_postal)})
        return HttpResponse(data)


