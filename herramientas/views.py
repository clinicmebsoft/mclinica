
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, StreamingHttpResponse, response
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json
import re
from unicodedata import normalize
from django.utils.encoding import  smart_str,iri_to_uri

# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from pyparsing import basestring, unicode

from citas.models import Cita
from herramientas.models import Codigo_postal
from mebClinic.settings import BASE_DIR


def agenda(request):
    return render(request, "herramientas/agenda.html")


def configuracion(request):
    return render(request,"configuracion.html")

def administracion(request):
    return render(request, "panelcontrol/administracion.html")

def to_unicode_or_bust(obj, encoding="latin1"):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj=unicode(obj, encoding)
    return obj
import codecs

@csrf_exempt
def cargaCP(reuest):
    #guarde el archivo en modo utf-8 con el editor
    filecp = codecs.open('static/text/cp.txt',  'r', 'UTF-8')
    cp = Codigo_postal()
    index = 0
    for line in filecp:
        fields = line.split('|')
        #print(fields[0])
        #s = to_unicode_or_bust(fields[1])
        #print(s)
        print(str(index))
        cp.pk = None
        cp.d_codigo = fields[0]
        cp.d_asenta = fields[1]
        cp.d_tipo_asenta = fields[2]
        cp.d_mnpio = fields[3]
        cp.d_estado = fields[4]
        cp.d_ciudad = fields[5]
        cp.d_cp = fields[6]
        cp.c_estado = fields[7]
        cp.c_oficina = fields[8]
        cp.c_cp = fields[9]
        cp.c_tipo_asenta = fields[10]
        cp.c_mnpio = fields[11]
        cp.id_asenta_cpcons = fields[12]
        cp.d_zona = fields[13]
        cp.c_cve_ciudad = fields[14]
        cp.save(force_insert=True)
        cp.clean()
        index = index+1
    filecp.close()

    return JsonResponse({
        'respuesta': {
            'mensaje': str(index) + ' registros guardados'
        }
    })

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


