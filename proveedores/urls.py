from django.urls import path, include
from . import views



urlpatterns = [
    path('proveedores/proveedor', views.proveedores, name='proveedores'),
    path('proveedores/laboratorios', views.laboratorios, name='laboratorios'),
    path('busca_cp',views.ax_buscar_cp,name='buscacp'), # está en la view de herramientas
    ]