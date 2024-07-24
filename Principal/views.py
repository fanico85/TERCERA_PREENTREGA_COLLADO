from Principal.models import Usuario
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def usuario(request, nombre, usuario):
    usuario = Usuario(nombre=nombre, usuario=usuario)
    usuario.save()
    lista = f"Nombres: {usuario.nombre}<br>Usuario: {usuario.camada}"
    return HttpResponse(lista)

def inicio(request):
    return render(request, "Principal/index.html")

def usuarios(request):
    return render(request, "Principal/usuarios.html")
