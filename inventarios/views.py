from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from inventarios.models import *
from proveedores.models import Proveedores
import json
from decimal import Decimal
from django.core import serializers


# Create your views here.
def inventarios(request):
    return render(request, "inventario.html")


def productos(request):
    return render(request, "productos.html")


def lista_articulos(request):
    return render(request, "lista_articulos.html")


def lista_precios(request):
    lista_precios = Articulos.objects.filter()
    contexto = {
        'listaprecios' : lista_precios,
    }
    return render(request, "lista_precios.html",contexto)


def ajax_abcGuardarCatalogos(request):
    salida = []

    json_data = json.loads(request.body)
    if request.is_ajax():
        que = json_data['que']
        id = json_data['id']
        desc = json_data['descripcion']

        descripcion = desc
        tipo = json_data['tipo']

        if tipo == "Categorias":
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
                    mod.pocentaje = porcentaje
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
        if tipo == "Proveedor":
            proveedor = Proveedores()
            proveedor.descripcion = descripcion
            if Proveedores.objects.filter(id=id).first():
                if que == 'M':
                    mod = Proveedores.objects.filter(id=id).first()
                    mod.descripcion = desc
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

                proveedor.save()
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
    unidades = Unidades.objects.filter().all().values('id', 'descripcion', 'estatus')
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
    impuesto = Impuestos.objects.filter(estatus='A').all().values('id', 'descripcion', 'porcentaje', 'estatus')
    data = json.dumps({"data": list(impuesto)})
    return HttpResponse(data)


def ajax_catalogo_proveedores(request):
    data_prov = []
    proveedor = Proveedores.objects.filter(estatus='A').all().values('id', 'razon_social', 'nombre', 'apellidos',
                                                                     'estatus')
    for prov in proveedor:
        dic = {}
        dic['id'] = prov['id']
        if prov['razon_social'] == '':
            dic['descripcion'] = prov['nombre'] + " " + prov['apellidos']
        else:
            dic['descripcion'] = prov['razon_social']
        data_prov.append(dic)

    data = json.dumps({"data": list(data_prov)})
    return HttpResponse(data)


def ajax_catalogo_lista_articulos(request):
    articulos = Articulos.objects.filter(estatus='A').all().values('id', 'codigo', 'codigobarras', 'descripcion',
                                                                   'estatus')
    data = json.dumps({"data": list(articulos)})
    return HttpResponse(data)


def ax_guardarArticulos(request):
    salida = ""
    json_data = json.loads(request.body)
    articulo = Articulos()
    if request.is_ajax():
        que = json_data['tipoMov']
        id = json_data['id']
        if que != 'C':
            if que == 'M':
                Articulos.objects.filter(id=id).first()
            articulo.tipo = json_data['tipo']
            articulo.clave = json_data['clave']
            articulo.descripcion = json_data['descripcion']
            articulo.codigobarras = json_data['codigobarras']
            articulo.id_categoria = Categorias.objects.get(id=int(json_data['id_categoria']))
            articulo.id_unidades = Unidades.objects.get(id=int(json_data['id_unidades']))
            articulo.id_marcas = Marcas.objects.get(id=int(json_data['id_marcas']))
            articulo.id_fabricantes = Fabricantes(id=int(json_data['id_fabricantes']))
            articulo.precioventa = json_data['precioventa']
            articulo.costo = json_data['costo']
            articulo.stock_max = json_data['stock_max']
            articulo.reorden = json_data['reorden']
            articulo.cantidad = json_data['cantidad']
            articulo.id_impuestos = Impuestos(id=int(json_data['id_impuestos']))
            articulo.id_proveedores = Proveedores(id=int(json_data['id_proveedores']))
            articulo.compuesto = json_data['compuesto']
            # articulo.id_compuesto = Compuesto.objects.get(id=int(json_data['id_compuesto']))
            articulo.save()
            salida = 'Se guardó artículo ' + json_data['descripcion']
        else:
            Articulos.objects.filter(id=id).first()
            articulo.estatus = 'C'
            articulo.save()
            salida = 'Se mordificó artículo ' + json_data['descripcion']
    else:
        salida = 'Error al guardar el registro'

    return JsonResponse({
        'respuesta': {
            'mensaje': salida
        }
    })
