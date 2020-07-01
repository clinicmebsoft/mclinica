from django.urls import path, include
from . import views


urlpatterns = [
    #/principal
    path('', views.index, name='index'), #las urls de pacintes
    path('pacientes/listapacientes',views.listapacientes,name='listapacientes'),
    path('pacientes/historiaclinica',views.historiaclinica,name='historiaclinica'),
    path('ajax_guardapaciente',views.ajax_guardapaciente,name='guardapacientes'),
    path('ax_CargaTpacientes',views.ax_CargaTpacientes,name='listapacientes'),
]