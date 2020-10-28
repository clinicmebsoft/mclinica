from django.urls import path, include
from . import views


urlpatterns = [
    #/principal
    path('', views.index, name='index'), #las urls de pacintes
    path('listapacientes',views.listapacientes,name='listapacientes'),
    path('historiaclinica/<int:id>',views.historiaclinica,name='historiaclinica'),
    path('ajx_guarda_historia',views.ajx_guarda_historia,name='ajx_guarda_historia'),

    path('edit_historiaclinica/<int:id>',views.edit_historiaclinica,name='edit_historiaclinica'),
    path('ajax_guardapaciente',views.ajax_guardapaciente,name='guardapacientes'),
    path('ax_CargaTpacientes',views.ax_CargaTpacientes,name='listapacientes'),
    path('ax_Presupuesto', views.ax_Presupuesto, name='guardapresupuesto'),

    path('edit_paciente/<int:id>',views.edit_paciente,name='edit_paciente'),
    path('pacientes/<int:id>',views.pacientes,name='pacientes'),

]