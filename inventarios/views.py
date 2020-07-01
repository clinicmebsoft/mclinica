from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from inventarios.models import *
import json
from decimal import Decimal
from django.core import serializers


# Create your views here.
def inventarios(request):
    return render(request, "inventarios/inventario.html")


def productos(request):
    return render(request, "inventarios/productos.html")


def lista_articulos(request):
    return render(request, "inventarios/lista_articulos.html")


def ajax_abcGuardarCatalogos(request):
    salida = []

    json_data = json.loads(request.body)
    if request.is_ajax():
        que = json_data['que']
        id = json_data['id']
        desc = json_data['descripcion']

        descripcion = desc
        tipo = json_data['tipo']

        if tipo=="Categorias":
            cate = Categorias()
            cate.descripcion = descripcion
            if Categorias.objects.filter(id=id).first():
                if que == 'M':
                    mod = Categorias.objects.filter(id=id).first()
                    mod.descripcion = desc
                    mod.save()
                    salida = "Registro {" + tipo + "} " + descripcion + " Modificado..."

                else:
                    if que == 'C':
                        mod = Categorias.objects.filter(id=id).first()
                        mod.estatus = 'C'
                        mod.save()
                        salida = "Registro {" + tipo + "} " + descripcion + " Se Canceló..."
                    else:
                        salida = "Error: Ya existe un registro similar"
            else:
                cate.save()
                salida = "Registro {" + tipo + "} " + descripcion + " Guardado..."
        if tipo == "Unidades":
            uni = Unidades()
            uni.descripcion = descripcion
            if Unidades.objects.filter(id=id).first():
                if que == 'M':
                    mod = Unidades.objects.filter(id=id).first()
                    mod.descripcion = desc
                    mod.save()
                    salida = "Registro {" + tipo + "} " + descripcion + " Modificado..."

                else:
                    if que == 'C':
                        mod = Unidades.objects.filter(id=id).first()
                        mod.estatus = 'C'
                        mod.save()
                        salida = "Registro {" + tipo + "} " + descripcion + " Se Canceló..."
                    else:
                        salida = "Error: Ya existe un registro similar"
            else:
                uni.save()
                salida = "Registro {" + tipo + "} " + descripcion + " Guardado..."
        if tipo == "Marcas":
            marcas = Marcas()
            marcas.descripcion = descripcion
            if Marcas.objects.filter(id=id).first():
                if que == 'M':
                    mod = Marcas.objects.filter(id=id).first()
                    mod.descripcion = desc
                    mod.save()
                    salida = "Registro {" + tipo + "} " + descripcion + " Modificado..."

                else:
                    if que == 'C':
                        mod = Marcas.objects.filter(id=id).first()
                        mod.estatus = 'C'
                        mod.save()
                        salida = "Registro {" + tipo + "} " + descripcion + " Se Canceló..."
                    else:
                        salida = "Error: Ya existe un registro similar"
            else:
                marcas.save()
                salida = "Registro {" + tipo + "} " + descripcion + " Guardado..."
        if tipo == "Fabricantes":
            fabricante = Fabricantes()
            fabricante.descripcion = descripcion
            if Fabricantes.objects.filter(id=id).first():
                if que == 'M':
                    mod = Fabricantes.objects.filter(id=id).first()
                    mod.descripcion = desc
                    mod.save()
                    salida = "Registro {" + tipo + "} " + descripcion + " Modificado..."

                else:
                    if que == 'C':
                        mod = Fabricantes.objects.filter(id=id).first()
                        mod.estatus = 'C'
                        mod.save()
                        salida = "Registro {" + tipo + "} " + descripcion + " Se Canceló..."
                    else:
                        salida = "Error: Ya existe un registro similar"
            else:
                fabricante.save()
                salida = "Registro {" + tipo + "} " + descripcion + " Guardado..."
        if tipo == "Impuestos":
            porcentaje = float(json_data['porcentaje'])
            impuesto = Impuestos()
            impuesto.descripcion = descripcion
            impuesto.porcentaje = porcentaje
            if Impuestos.objects.filter(id=id).first():
                if que == 'M':
                    mod = Impuestos.objects.filter(id=id).first()
                    mod.descripcion = desc
                    mod.pocentaje=porcentaje
                    mod.save()
                    salida = "Registro {" + tipo + "} " + desc + " Modificado..."

                else:
                    if que == 'C':
                        mod = Impuestos.objects.filter(id=id).first()
                        mod.estatus = 'C'
                        mod.save()
                        salida = "Registro {" + tipo + "} " + descripcion + " Se Canceló..."
                    else:
                        salida = "Error: Ya existe un registro similar"
            else:

                impuesto.save()
                salida = "Registro {" + tipo + "} " + descripcion + " Guardado..."
    else:
        salida = 'Error al guardar el registro'

    return JsonResponse({
        'respuesta': {
            'mensaje': salida
        }
    })


def ajax_catalogo_listcategoria(request):
    categoria = Categorias.objects.filter(estatus='A').all().values('id', 'descripcion', 'estatus')
    data = json.dumps({"data": list(categoria)})
    return HttpResponse(data)


def ajax_catalogo_unidad(request):
    unidades = Unidades.objects.filter(estatus='A').all().values('id', 'descripcion', 'estatus')
    data = json.dumps({"data": list(unidades)})
    return HttpResponse(data)

def ajax_catalogo_marca(request):
    marcas = Marcas.objects.filter(estatus='A').all().values('id', 'descripcion', 'estatus')
    data = json.dumps({"data": list(marcas)})
    return HttpResponse(data)

def ajax_catalogo_fabricante(request):
    fabricante = Fabricantes.objects.filter(estatus='A').all().values('id', 'descripcion', 'estatus')
    data = json.dumps({"data": list(fabricante)})
    return HttpResponse(data)

def ajax_catalogo_impuesto(request):
    impuesto = Impuestos.objects.filter(estatus='A').all().values('id', 'descripcion', 'porcentaje','estatus')
    data = json.dumps({"data": list(impuesto)})
    return HttpResponse(data)



def ajax_catalogo_lista_articulos(request):
    articulos = Articulos.objects.filter(estatus='A').all().values('id', 'codigo', 'codigobarras', 'descripcion',
                                                                   'estatus')
    data = json.dumps({"data": list(articulos)})
    return HttpResponse(data)
