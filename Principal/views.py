from Principal.models import Usuario, Servicio
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Principal.forms import ServicioFormulario
from django.contrib import messages

# Create your views here.
def usuario(request, nombre, usuario):
    usuario = Usuario(nombre=nombre, usuario=usuario)
    usuario.save()
    lista = f"Nombres: {usuario.nombre}<br>Usuario: {usuario.camada}"
    return HttpResponse(lista)

def inicio(request):
    return render(request, "Principal/index.html")

def servicios(request):
    return render(request, "Principal/servicios.html")

def servicio_formulario(request):
    if request.method == "POST":
        mi_formulario = ServicioFormulario(request.POST) #Aqui me llega la info del html
        #print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            servicio = Servicio(nombre = informacion["nombre_servicio"],descripcion = informacion["descripcion"])
            servicio.save()

            messages.success(request, 'Servicio agregado')
            return redirect('Inicio')
            #return render(request, "Principal/index.html")
            #return render(request, "Principal/servicio_form.html")
            #return render(request, "Principal/servicio_form.html", {"mi_formulario":mi_formulario})
    else:
        mi_formulario = ServicioFormulario()
        
    return render(request, "Principal/servicio_form.html", {"mi_formulario":mi_formulario})

def servicio_formulario_busqueda(request):
    return render(request, "Principal/servicio_busqueda.html")

def servicio_buscar(request):
    if request.GET['nombre']:
        #respuesta = f"Estoy buscando el servicio {request.GET['nombre']}"
        nombre = request.GET['nombre']
        servicios = Servicio.objects.filter(nombre__icontains=nombre)
        return render(request,"Principal/resultadoBusquedaServicio.html",{"nombre":nombre, "servicios":servicios})

    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)