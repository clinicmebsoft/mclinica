from django.urls import path, include
from . import views


urlpatterns = [
    #/principal
    path('', views.personal, name='personal'), #las urls de personal

    path('ax_guardaespecialidad',views.ax_guardaespecialidad,name='ax_guardaespecialidad')
]