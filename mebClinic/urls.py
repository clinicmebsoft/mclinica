"""mebClinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
urlpatterns = [


    path('', include('principal.urls')),
    path('principal/', include('principal.urls')),

    path('', include('pacientes.urls')),
    path('pacientes/', include('pacientes.urls')),

    path('', include('citas.urls')),
    path('citas/', include('citas.urls')),


    path('', include('inventarios.urls')),
    path('inventarios/', include('inventarios.urls')),

    path('', include('herramientas.urls')),
    path('herramientas/', include('herramientas.urls')),

    path('', include('ventas.urls')),
    path('ventas/', include('ventas.urls')),

    path('', include('proveedores.urls')),
    path('proveedores/', include('proveedores.urls')),

    path('', include('caja.urls')),
    path('caja/', include('caja.urls')),

    path('',include('Personal.urls')),
    path('personal/',include('Personal.urls')),

    path('admin/', admin.site.urls)
]
