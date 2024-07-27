from Principal.models import Usuario, Servicio, Gasto
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Principal.forms import ServicioFormulario, GastoFormulario, ServicioBuscar
from django.contrib import messages

# Create your views here.
def usuario(request, nombre, usuario):
    usuario = Usuario(nombre=nombre, usuario=usuario)
    usuario.save()
    lista = f"Nombres: {usuario.nombre}<br>Usuario: {usuario.camada}"
    return HttpResponse(lista)

def inicio(request):
    return render(request, "Principal/index.html")

def tablas(request):
    return render(request, "Principal/tables.html")

def servicios(request):
    return render(request, "Principal/servicios.html")

def servicio_formulario(request):
    if request.method == "POST":
        mi_form = ServicioFormulario(request.POST) #Aqui me llega la info del html
        #print(mi_formulario)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            servicio = Servicio(ser_nombre = info["servicio_nombre"],ser_descripcion = info["servicio_descripcion"], ser_duracion = info["servicio_duracion"])
            servicio.save()

            #messages.success(request, 'Servicio agregado')
            #return redirect('Inicio')
            #return render(request, "Principal/index.html")
            #return render(request, "Principal/servicio_form.html")
            mi_form = ServicioFormulario()
            return render(request, "Principal/servicio_agregar.html", {"mi_formulario":mi_form})
    else:
        mi_form = ServicioFormulario()
        
    return render(request, "Principal/servicio_agregar.html", {"mi_formulario":mi_form})

def gasto_formulario(request):
    if request.method == "POST":
        mi_form = GastoFormulario(request.POST) #Aqui me llega la info del html
       
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            gasto = Gasto(gas_nombre = info["gasto_nombre"],gas_descripcion = info["gasto_descripcion"], gas_monto = info["gasto_monto"], gas_fecha = info["gasto_fecha"])
            gasto.save()
            
            mi_form = GastoFormulario()
            return render(request, "Principal/gasto_agregar.html", {"mi_formulario":mi_form})
    else:
        mi_form = GastoFormulario()
        
    return render(request, "Principal/gasto_agregar.html", {"mi_formulario":mi_form})

def servicio_buscar(request):    
    if request.method == "POST":
        mi_form = ServicioBuscar(request.POST)

        if mi_form.is_valid():
            info = mi_form.cleaned_data

            servicios =  Servicio.objects.filter(ser_nombre__icontains=info["servicio_nombre"])

            return render(request, "Principal/resultadoBusquedaServicio.html",{"servicios":servicios, "servicio_nombre": info["servicio_nombre"]})
    
    else:
        mi_form = ServicioBuscar()

    return render(request, "Principal/servicio_buscar.html",{"mi_formulario":mi_form})

    