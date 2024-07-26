from django.urls import path
from Principal.views import inicio, servicios
from django.contrib import admin

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('servicios/',servicios,name="Servicios")
]
