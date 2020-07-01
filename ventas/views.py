from django.shortcuts import render

# Create your views here.

def presupusto(request):
    return render(request, "ventas/presupuesto.html")