from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_protect

from personal.models import Especialidad,Doctores


def personal(request):  # usuario no activo mandar al login
    return render(request, "personal.html")

def login(request):  # usuario no activo mandar al login
    return render(request, "login.html")


@csrf_protect
def ax_dameDetallePersonal(request):
    resp = ''
    if request.method == 'POST' and request.is_ajax:
        row = json.loads(request.body)

        if Doctores.objects.filter(id=row['id']).count()>0:
            detallePersonal = Doctores.objects.get(id=row['id'])
            detalle = []
            d_json = {}
            d_json['nombre'] = detallePersonal.nombre
            d_json['apellidos']=detallePersonal.apellidos
            d_json['correo'] = detallePersonal.correo
            d_json['fechaNat']=detallePersonal.fecha_nat
            d_json['sexo']=detallePersonal.sexo
            d_json['especialidad']=detallePersonal.especialidad_id
            d_json['cp']=detallePersonal.cp
            d_json['calle']=detallePersonal.callenum
            d_json['colonia']=detallePersonal.colonia
            d_json['telefono'] = detallePersonal.telefono_particular
            d_json['celular'] = detallePersonal.celular
            d_json['ciudad'] = detallePersonal.ciudad
            d_json['estado'] = detallePersonal.estado
            d_json['pais'] = detallePersonal.pais
            d_json['observaciones'] = detallePersonal.observaciones
            d_json['estatus']=detallePersonal.estatus
            detalle.append(d_json)
            resp = detalle
        else:
            resp = "No encontré el registro..."
    mimetype = 'application/json'
    return JsonResponse({
        'respuesta': {
            'detallePersonal': resp
        }
    })

@csrf_protect
def ax_getListaPersonal(request):
    lista_personal = Doctores.objects.all();
    lpersonal = []
    for lp in lista_personal:
        l_json = {}
        l_json['id'] = lp.id
        l_json['nombre'] = lp.nombre
        l_json['apellidos'] = lp.apellidos
        l_json['especialidad'] = lp.especialidad.especialidad
        lpersonal.append(l_json)

    mimetype = 'application/json'
    return JsonResponse({
        'respuesta': {
            'listaPersonal': lpersonal
        }
    })


@csrf_protect
def ax_getespecialidad(request):
    esp = Especialidad.objects.filter(estatus='A')
    especialidades = []
    for e in esp:
        p_json = {}
        p_json['id'] = e.id
        p_json['especialidad'] = e.especialidad
        especialidades.append(p_json)

    mimetype = 'application/json'
    return JsonResponse({
        'respuesta': {
            'esp': especialidades
        }
    })
@csrf_protect
def ax_guardaespecialidad(request):
    resp = ''
    esp = Especialidad()
    if request.method == 'POST' and request.is_ajax:
        row = json.loads(request.body)
        esp.especialidad = row['esp']
        esp.save()
        resp="Especialidad ha sido guardada..."

    return JsonResponse({
        'respuesta': resp,

    })
@csrf_protect
def ax_guardaPersonal(request):
    resp = ''

    doc = Doctores()
    if request.method == 'POST' and request.is_ajax:
        row = json.loads(request.body)
        if row['tipo']=='N':
            if Doctores.objects.filter(nombre=row['nombre'],apellidos=row['apellidos']):
                return JsonResponse({
                    'respuesta': {
                        'mensaje': "Error ya existe un registro con este nombre "+row['nombre']+" "+row['apellidos']
                    }
                })
        else:
            if not Doctores.objects.filter(nombre=row['nombre'],apellidos=row['apellidos']):
                return JsonResponse({
                    'respuesta': {
                        'mensaje': "Error el registro ya no existe..."
                    }
                })

        getesp = Especialidad.objects.get(id=row['especialidad'])
        doc.nombre = row['nombre']
        doc.apellidos = row['apellidos']
        doc.correo = row['correo']
        doc.fecha_nat = row['fechaNat']
        doc.sexo = row['sexo']
        doc.especialidad = getesp
        doc.cp = row['cp']
        doc.callenum = row['callenum']
        doc.colonia = row['colonia']
        doc.telefono = row['telefono']
        doc.celular = row['celular']
        doc.ciudad = row['ciudad']
        doc.estado = row['estado']
        doc.pais = row['pais']
        doc.observaciones = row['observaciones']
        doc.estatus  = row['estatus'][0:1]
        doc.save()
        resp= 'Registro se ha guardado con éxito...'
    else:
        resp = "Error al intentar guardar el registro"
    mimetype = 'application/json'
    return JsonResponse({
        'respuesta': {
            'mensaje': resp
        }
    })