from django.urls import path, include
from . import views


urlpatterns = [
    #/principal
    path('', views.index, name='index'),
    path('carga',views.cargacards,name="cargacards")
]