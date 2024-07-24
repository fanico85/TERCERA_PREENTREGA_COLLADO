from django.urls import path
from Principal.views import inicio, usuarios
from django.contrib import admin

urlpatterns = [
    path("", inicio),
    path('usuarios/',usuarios,name="Usuarios")
]
