from django.urls import path
from Principal import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('servicios/',views.servicios,name="Servicios")
]

nuevas_urls = [
    path('servicio-formulario/',views.servicio_formulario, name = "ServicioFormulario"),
    path('servicio-formulario-busqueda/',views.servicio_formulario_busqueda, name = "ServicioFormularioBusqueda"),
    path('servicio-buscar/',views.servicio_buscar, name = "ServicioBuscar")
]

urlpatterns += nuevas_urls 