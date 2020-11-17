
from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from Personal.models import Especialidad


def personal(request):  # usuario no activo mandar al login
    return render(request, "personal.html")


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