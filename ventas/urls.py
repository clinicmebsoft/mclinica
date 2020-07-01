from django.urls import path, include
from . import views


urlpatterns = [
    path('ventas/presupuesto', views.presupusto, name='ventas'),
    ]