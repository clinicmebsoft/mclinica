from django.urls import path
from . import views



urlpatterns = [
    #/principal
    path('', views.personal, name='personal'), #las urls de personal
    path('login', views.login, name='login'),
    path('ax_guardaespecialidad',views.ax_guardaespecialidad,name='ax_guardaespecialidad'),
    path('ax_getespecialidad',views.ax_getespecialidad,name='ax_getespecialidad'),
    path('ax_guardaPersonal',views.ax_guardaPersonal,name='ax_guardaPersonal'),
    path('ax_getListaPersonal',views.ax_getListaPersonal,name='ax_getListaPersonal'),
    path('ax_dameDetallePersonal',views.ax_dameDetallePersonal,name='ax_dameDetallePersonal'),
]