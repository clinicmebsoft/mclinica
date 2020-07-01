from django.urls import path, include
from . import views

urlpatterns = [
    path('citas/cita', views.index, name='index'),
    path('ajax_obtenDatosPacienteCitas',views.ajax_obtenDatosPacienteCitas,name='obtendatospaciente'),
    path('ajax_BuscaPacientes',views.ajax_BuscaPacientes,name="buscapacientes"),
    path('guardacitas',views.guardacitas,name='guardacita'),
]