from django.urls import path, include
from . import views


urlpatterns = [
    path('inventarios/', views.inventarios, name='inventarios'),
    path('inventarios/productos', views.productos, name='productos'),
    path('ajax_abcGuardarCatalogos' , views.ajax_abcGuardarCatalogos, name='abcGuardarCatalogos'),
    path('inventarios/lista_articulos', views.lista_articulos, name='lista_articulos'),

    path('ajax_catalogo_listcategoria',views.ajax_catalogo_listcategoria, name='catalogo_categorias'),
    path('ajax_catalogo_unidad',views.ajax_catalogo_unidad, name = "catalogo_unidad"),
    path('ajax_catalogo_marca' , views.ajax_catalogo_marca, name='ajax_catalogo_marca'),
    path('ajax_catalogo_fabricante' , views.ajax_catalogo_fabricante, name='ajax_catalogo_fabricante'),
    path('ajax_catalogo_impuesto' , views.ajax_catalogo_impuesto, name='ajax_catalogo_impuesto'),

    ]


