from django.http import JsonResponse
from django.shortcuts import render
from herramientas.views import ax_buscar_cp
from proveedores.models import *
import json


# Create your views here.

def proveedores(request):
    return render(request, "proveedores/proveedor.html")


def laboratorios(request):
    return render(request, "proveedores/laboratorios.html")


def ajax_abcGuardarProveedor(request):
    salida = ""
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body)
        razonsocial = json_data['razon_social']
        nombre = json_data['nombre']
        apellidos = json_data['apellidos']
        tipo = json_data['tipo']
        proveedor = Proveedores()
        try:
            if Proveedores.objects.filter(razon_social=razonsocial, nombre=nombre,
                                          apellidos=apellidos).first() and tipo == 'G':
                salida = 'Existe un proveedor con esa información'
            else:
                if tipo == 'M':
                    Proveedores.objects.filter(razon_social=razonsocial, nombre=nombre, apellidos=apellidos).first()
                    proveedor.cp = json_data['cp']
                    proveedor.estado = json_data['estado']
                    proveedor.ciudad = json_data['ciudad']
                    proveedor.municipio = json_data['municipio']
                    proveedor.colonia = json_data['colonia']
                    proveedor.calle = json_data['calle']
                    proveedor.telefono = json_data['telefono']
                    proveedor.celular = json_data['celular']
                    proveedor.email = json_data['email']
                    proveedor.web = json_data['web']
                    proveedor.objects = json_data['observaciones']
                    proveedor.save()
                    salida = "Registro Nodificado..."
                else:
                    if tipo == 'C':
                        Proveedores.objects.filter(razon_social=razonsocial, nombre=nombre, apellidos=apellidos).first()
                        proveedor.estatus = 'C'
                    else:
                        proveedor.razon_social = json_data['razon_social']
                        proveedor.nombre = json_data['nombre']
                        proveedor.apellidos = json_data['apellidos']
                        proveedor.cp = json_data['cp']
                        proveedor.estado = json_data['estado']
                        proveedor.ciudad = json_data['ciudad']
                        proveedor.municipio = json_data['municipio']
                        proveedor.colonia = json_data['colonia']
                        proveedor.calle = json_data['calle']
                        proveedor.telefono = json_data['telefono']
                        proveedor.celular = json_data['celular']
                        proveedor.email = json_data['email']
                        proveedor.web = json_data['web']
                        proveedor.observaciones = json_data['observaciones']
                        proveedor.save()
                        salida = "Registro Guardado..."
        except:
            salida = "Error al " + tipo + " registro"

    return JsonResponse({
        'respuesta': {
            'mensaje': salida,
        }
    })
