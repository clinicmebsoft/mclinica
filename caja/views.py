from django.shortcuts import render

# Create your views here.
def abrircaja(request):
    return render(request, "caja/abrircaja.html")