from django.urls import path, include
from . import views


urlpatterns = [
    path('caja/abrircaja', views.abrircaja, name='caja'),

    ]