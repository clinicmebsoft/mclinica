import datetime

from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, response
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from Personal.models import Doctores,Especialidad
from pacientes.models import Paciente, PacienteForm, HistoriaClinicaForm, HistoriaClinica, \
     ListaTratamientos, PresuPaciente, PresuPacienteDetalle

from django.core import serializers
from inventarios.models import Articulos
import json

# Create your views here.



def index(request):  # usuario no activo mandar al login
    return render(request, "paciente.html")


def nuevo_paciente(request):
    if request.method == 'POST':
        selected_option = request.POST.get('sexo', None)
        form = PacienteForm(request.POST or None)
        if form.is_valid():
            form.fields['sexo'] = selected_option
            form.fields['estatus'] = "A"
            form.save()
            messages.success(request, 'Registro Guardado')
    return render(request, 'paciente.html')


def listapacientes(request):
    lpacientes = Paciente.objects.filter().order_by('id').reverse()
    context = {
        'lpacientes': lpacientes,
    }
    return render(request, "listapacientes.html", context)


def edit_paciente(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        selected_option = request.POST.get('sexo', None)
        instance = Paciente.objects.get(id=id)
        form = PacienteForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.fields['sexo'] = selected_option
            form.fields['estatus'] = "A"
            form.fields['celular2'] = request.POST.get('celular2')
            form.save(commit=True)
            messages.success(request, 'Datos actualizados')
        return HttpResponseRedirect(url)
    else:
        paciente = Paciente.objects.get(id=id)
        form = PacienteForm()
        context = {
            'paciente': paciente,
            'form': form,
        }
        return render(request, 'edit_paciente.html', context)


def edit_historiaclinica(request, id):
    url = request.META.get('HTTP_REFERER')
    paciente = Paciente.objects.get(id=id)
    if request.method == 'GET':
        form_hc = HistoriaClinicaForm(instance=paciente)
    else:
        form_hc = HistoriaClinicaForm(request.POST, instance=paciente)
        if form_hc.is_valid():
            form_hc.cleaned_data['id_paciente'] = id

            form_hc.save()
            messages.success(request, 'Registro Guardado')
        else:
            messages.success(request, 'Error al intentar guardar el registro...')

    form_hc = HistoriaClinicaForm(instance=paciente)
    context = {
        'paciente': paciente,
        'form_hc': form_hc,
    }
    return render(request, "edit_historiaclinica.html", context)


def historiaclinica(request, id):
    url = request.META.get('HTTP_REFERER')

    paciente = Paciente.objects.filter(id=id)
    nombrepaciente = paciente[0].nombre + " " + paciente[0].apellidos
    articulos = Articulos.objects.filter(tipo='Servicio')
    try:
        hc = HistoriaClinica.objects.get(id_paciente=id)
        existeHC = 1
        context = {
            'id': id,
            'nombre': nombrepaciente,
            'existeHC': existeHC,
            'articulos': articulos,
            'hc': hc,
        }
    except HistoriaClinica.DoesNotExist:
        existeHC = 0
        context = {
            'id': id,
            'nombre': nombrepaciente,
            'existeHC': existeHC,
            'articulos': articulos,

        }

    return render(request, "historiaclinica.html", context)


# https://pytutorial.com/how-to-make-a-pagination-with-django-and-ajaxjquery
def ajx_guarda_historia(request):
    resp = ""
    if request.is_ajax():
        try:
            json_data = json.loads(request.body)
            paciente = Paciente.objects.get(id=json_data['id'])
            HC = HistoriaClinica()
            HC.id_paciente = paciente

            originario = json_data['origin']
            medi = json_data['medi']
            telmed = json_data['telmed']
            cirugia = json_data['cirugia']

            HC.originario = originario
            HC.medico_particular = medi
            HC.telefono_medico = telmed
            HC.cirugias = cirugia
            HC.motivo_cita = json_data['motivo']
            HC.enfermedad_ultimo_anos = json_data['enfermedadUiltimosA']
            HC.enfermedad_grave = json_data['EnfermedadGrave']
            HC.Cirugia = json_data['Cirugia']
            HC.traumatismos_secuelas = json_data['TraumatismoSecuelas']
            HC.transfusiones = json_data['Transfusiones']
            HC.hemorragias = json_data['Hemorragias']
            HC.donador_sangre = json_data['DonadorSangre']
            HC.accidentes_tratamientos = json_data['AccidenteTratamientos']
            HC.toma_medicamento = json_data['TomaMedicamento']
            HC.enfermedades = json_data['Enfermedades']
            HC.familiar_enfermedad = json_data['Familiar']
            # HC. json_data['AlguienEnfermo']
            HC.embarazada = json_data['Embarazada']
            HC.higiene = json_data['Higiene']
            HC.numero_cepillados = json_data['CepilladosDia']
            HC.alimentacion = json_data['Alimentacion']
            HC.integrantes_casa = json_data['Integrantes']
            HC.practica_deportes = json_data['Deporte']
            HC.habito_adiccion = json_data['Habito']
            HC.temperatura = int(json_data['Temperatura'])
            HC.presion = json_data['Presion']
            HC.pulso = int(json_data['Pulso'])
            HC.tratamientos_odontologicos = json_data['TratamientoReciente']
            HC.alergico_anestesia = json_data['Alergico']
            HC.experiencia_tratamientos = json_data['Experiencia']
            HC.articulacion_temporo = json_data['ArticulacionTemporoMandibular']
            HC.dolor_articulacion = json_data['DolorArticulacion']
            HC.chasquidos = json_data['ChasquidosRuidos']
            HC.limitacion_apertura = json_data['LimitacionApertura']
            HC.limitacion_movimientos = json_data['LimitacionMovimientos']
            HC.bruxismo = json_data['Bruxismo']
            HC.obervaciones = json_data['Observaciones']

            HC.save()
            resp = "Se guardó con éxito..."
        except Exception as e:
            resp = 'Error: ' + e.__str__()
    return JsonResponse({
        'respuesta': {
            'mensaje': resp
        }
    })


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


def pacientes(request, id):
    paciente = Paciente.objects.filter(id=id)
    existePac = 0
    if (paciente):
        existePac = 1
    context = {
        'existePac': existePac,
    }
    return render(request, 'paciente.html', context)


def ajax_guardapaciente(request):
    resp = ""
    paciente = Paciente()
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body)
        # print(json_data)
        # print(json_data['nombre'])
        nombre = json_data['nombre']
        apellidos = json_data['apellidos']
        correo = json_data['correo']
        if Paciente.objects.filter(nombre=nombre, apellidos=apellidos, correo=correo):
            resp = "Ya existe un paciente con ese nombre y correo"
        else:
            # print('nombre' + str(nombre))
            paciente.nombre = str.upper(nombre)
            paciente.apellidos = str.upper(apellidos)
            paciente.correo = correo
            paciente.ocupacion = json_data['ocupacion']

            paciente.fecha_nacimiento = json_data['fechanacimiento']
            paciente.edad = int(json_data['edad'])
            paciente.calle = json_data['calle']
            paciente.colonia = json_data['colonia']
            paciente.cp = json_data['cp']
            paciente.ciudad = json_data['ciudad']
            paciente.estado = json_data['estado']
            paciente.pais = json_data['pais']
            paciente.telefono = json_data['telefono']
            paciente.celular = json_data['celular']
            paciente.observaciones = json_data['comentario']
            paciente.sexo = json_data['sexo']

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
    pacientes = Paciente.objects.exclude(estatus='C').all().values('id', 'nombre', 'apellidos', 'calle', 'telefono',
                                                                   'celular', 'correo')
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


def ax_Presupuesto(request):
    resp = ""
    presupuesto = PresuPaciente()
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body)
        id_paciente = json_data['id_paciente']
        id_doctor = json_data['id_doctor']
        id_tratamiento = json_data['id_tratamiento']

        precio = json_data['precio']
        descuento = json_data['descuento']
        vence = datetime.datetime.now() + datetime.timedelta(30)  # sólo se respetan 30 días del presupuesto
        estatus = 'T'  # temporal puede pasar a P = presentado, después a A = aceptado
        presupuesto.save()
        print(json_data['id_paciente'])

    else:
        resp = "Error al guardar registro del presupuesto"

    return JsonResponse({
        'respuesta': {
            'mensaje': resp,
        }
    })


def ax_obtenPrecioTratamiento(request):
    resp = ""
    #presupuesto = Presupuesto()
    # articulos = Articulos()
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body)
        idTratamiento = json_data['id_tratamiento']
        articulos = Articulos.objects.get(id=idTratamiento)
        resp = articulos.precioventa
    else:
        resp = "Error al Obtener PrecioTratamiento"

    return JsonResponse({
        'respuesta': resp,

    })

@require_POST
def ax_guardaPresupuesto(request):
    if request.method=='POST' and request.is_ajax:
        rows = json.loads(request.body)

        try:
            with transaction.atomic():
                presupuesto = PresuPaciente()
                idpaciente=  rows['presu_data'][0]['id_paciente']
                idDoctor = rows['presu_data'][0]['id_doctor']
                presupuesto.id_paciente = Paciente.objects.get(id=idpaciente)
                presupuesto.id_doctor = Doctores.objects.get(id=idDoctor)
                presupuesto.descuento =0
                presupuesto.subtotal= 0
                presupuesto.total = rows['presu_data'][0]['total']
                presupuesto.vence = datetime.datetime.now() + datetime.timedelta(30)  # sólo se respetan 30 días del presupuesto
                presupuesto.estatus = 'T'  # temporal puede pasar a P = presentado, después a A = aceptado
                presupuesto.save()
                for datos in rows['presu_data']:
                    # print(value['id'])
                    presupuesto_detalle = PresuPacienteDetalle()
                    presupuesto_detalle.id_presupuesto=presupuesto.id
                    trata = Articulos.objects.get(id=datos['id'])
                    #presupuesto.id_paciente = paciente
                    #presupuesto.id_doctor = dr
                    presupuesto_detalle.id_tratamiento =trata
                    presupuesto_detalle.precio = datos['precio']
                    presupuesto_detalle.descuento = datos['descuento']


                    presupuesto.save()
                resp = 'Presupuesto Guardado'

        except Exception as e:
            transaction.rollback()
            resp = "Error al intentar guardar el presupuesto..."

    return JsonResponse({
        'respuesta': resp,

    })
