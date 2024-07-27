from django.urls import path
from Principal import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('servicios/',views.servicios,name="Servicios"),
    path('servicio-agregar/',views.servicio_formulario, name = "ServicioAgregar"),
    path('gasto-agregar/',views.gasto_formulario, name = "GastoAgregar")
]

nuevas_urls = [
    #path('servicio-formulario-busqueda/',views.servicio_formulario_busqueda, name = "ServicioFormularioBusqueda"),
    #path('servicio-buscar/',views.servicio_buscar, name = "ServicioBuscar"),
    path('servicio-buscar',views.servicio_buscar, name = "ServicioBuscar")
]

urls_pruebas = [
    path('tablas',views.tablas, name = "Tablas"),
]

urlpatterns += nuevas_urls 
urlpatterns += urls_pruebas
