
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import logout_then_login,auth_login
from django.contrib.auth import login


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

    path('', include('personal.urls')),
    path('personal/', include('personal.urls')),

    path('api/',include('api.urls')),
    path('admin/', admin.site.urls)
]
