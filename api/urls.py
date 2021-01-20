from django.urls import path
from . import views

from rest_framework import routers
from api.viewsets import DoctoresViewSet,CitaViewSet,ArticulosViewSet,EspecialidadesViewSet

route = routers.SimpleRouter()
route.register('personal',DoctoresViewSet)
route.register('especialidad',EspecialidadesViewSet)
route.register('cita',CitaViewSet)
route.register('articulos',ArticulosViewSet)

urlpatterns = route.urls