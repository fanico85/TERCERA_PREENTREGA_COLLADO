from django.urls import path
from Principal import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name="Inicio")
]

servicio_urls = [
    path('servicio-agregar/',views.servicio_formulario, name = "ServicioAgregar"),
    path('servicio-buscar/',views.servicio_buscar, name = "ServicioBuscar"),
    path('servicio-todos/',views.servicio_todos, name = "ServicioTodos")
]

gasto_urls = [
    path('gasto-todos/',views.gasto_todos, name = "GastoTodos"),
    path('gasto-agregar/',views.gasto_formulario, name = "GastoAgregar")
]

insumo_urls = [
    path('insumo-todos/',views.insumo_todos, name = "InsumoTodos"),
    path('insumo-agregar/',views.insumo_formulario, name = "InsumoAgregar")
]

otras_pruebas = [
    path('tablas/',views.tablas, name = "Tablas"),
    path('blanco/',views.blanco, name = "Blanco"),
]

urlpatterns += servicio_urls 
urlpatterns += gasto_urls
urlpatterns += insumo_urls
urlpatterns += otras_pruebas
