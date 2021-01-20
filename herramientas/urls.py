from django.urls import path, include
from . import views

urlpatterns = [
    path('agenda',views.agenda,name='agenda'),
    path('ax_agenda',views.ax_agenda,name='agenda'),
    path('ax_citas',views.ax_agenda,name='agenda'),
    path('ax_buscar_cp',views.ax_buscar_cp,name='buscar_cp'),
    path('panelcontrol/administracion',views.administracion,name='administracion'),
    path('ax_cargacp',views.cargaCP,name='cargaCP'),
    path('configuracion', views.configuracion,name='configuracion')
]