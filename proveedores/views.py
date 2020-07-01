from django.shortcuts import render
from herramientas.views import ax_buscar_cp
# Create your views here.

def proveedores(request):
    return render(request, "proveedores/proveedor.html")

def laboratorios(request):
    return render(request, "proveedores/laboratorios.html")

