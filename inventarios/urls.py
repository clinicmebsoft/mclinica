from django.urls import path, include
from . import views


urlpatterns = [
    path('inventarios', views.inventarios, name='inventarios'),
    path('productos', views.productos, name='productos'),
    path('lista_precios', views.lista_precios, name='lista_precios'),
    path('ajax_abcGuardarCatalogos' , views.ajax_abcGuardarCatalogos, name='abcGuardarCatalogos'),
    path('lista_articulos', views.lista_articulos, name='lista_articulos'),
    path('ax_guardarArticulos',views.ax_guardarArticulos,name = 'ax_guardarArticulos'),


    path('ajax_catalogo_listcategoria',views.ajax_catalogo_listcategoria, name='catalogo_categorias'),
    path('ajax_catalogo_unidad',views.ajax_catalogo_unidad, name = "catalogo_unidad"),
    path('ajax_catalogo_marca' , views.ajax_catalogo_marca, name='ajax_catalogo_marca'),
    path('ajax_catalogo_fabricante' , views.ajax_catalogo_fabricante, name='ajax_catalogo_fabricante'),
    path('ajax_catalogo_impuesto' , views.ajax_catalogo_impuesto, name='ajax_catalogo_impuesto'),
    path('ajax_catalogo_proveedores' , views.ajax_catalogo_proveedores, name='ajax_catalogo_proveedores'),

    path('ajax_catalogo_lista_articulos',views.ajax_catalogo_lista_articulos,name='catalogo_lista_articulos'),
    ]


