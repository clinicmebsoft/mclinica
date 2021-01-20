from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.proveedores, name='proveedores'),
    path('proveedor', views.proveedores, name='proveedores'),
    path('laboratorios', views.laboratorios, name='laboratorios'),

    path('busca_cp',views.ax_buscar_cp,name='buscacp'), # está en la view de herramientas
    path('ajax_abcGuardarProveedor',views.ajax_abcGuardarProveedor,name='GuardarProveedor'),
    ]