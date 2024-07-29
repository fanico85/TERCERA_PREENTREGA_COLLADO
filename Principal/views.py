from Principal.models import Usuario, Servicio, Gasto, Insumo, Stock
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Principal.forms import ServicioFormulario, GastoFormulario, ServicioBuscar, InsumoFormulario

# Create your views here.
def usuario(request, nombre, usuario):
    usuario = Usuario(nombre=nombre, usuario=usuario)
    usuario.save()
    lista = f"Nombres: {usuario.nombre}<br>Usuario: {usuario.camada}"
    return HttpResponse(lista)

def blanco(request):
    return render(request, "Principal/blanco.html")

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

            return render(request, "Principal/servicio_buscar_resultado.html",{"servicios":servicios, "servicio_nombre": info["servicio_nombre"]})
    
    else:
        mi_form = ServicioBuscar()

    return render(request, "Principal/servicio_buscar.html",{"mi_formulario":mi_form})

def servicio_todos(request):    
    if request.method == "GET":
        
        servicios =  Servicio.objects.all()

        return render(request, "Principal/servicio_todos.html",{"servicios":servicios})
    
def gasto_todos(request):    
    if request.method == "GET":
        
        gastos =  Gasto.objects.all() 
        contador = gastos.__len__()
        suma = 0

        for gasto in gastos:                     
            suma += gasto.gas_monto     
       
        return render(request, "Principal/gasto_todos.html",{"gastos":gastos, "contador":contador, "total":suma})
   
def inicio(request):    

    if request.method == "GET":

        #GASTOS
        print("llega")
        gastos = Gasto.objects.all()         
        suma = 0
        color_tarj_gastos = "card bg-primary text-white mb-4"        
       
        for gasto in gastos:                     
            suma += gasto.gas_monto     
        
        if suma > 6000 and suma < 10000:
            color_tarj_gastos = "card bg-warning text-white mb-4"
        elif suma > 10000:
            color_tarj_gastos = "card bg-danger text-white mb-4"

        #INSUMOS
        insumos =  Insumo.objects.filter(ins_stock__st_minimo__gte = F('ins_stock__st_actual'))
        cont_insumos = 0 
        print(cont_insumos)
        cont_insumos = insumos.__len__()     
        print(cont_insumos) 
        color_tarj_insumo = "card bg-primary text-white mb-4"

        if cont_insumos > 0:
            color_tarj_insumo = "card bg-danger text-white mb-4"

        #SERVICIOS   
        servicios = Servicio.objects.all()
        cont_servicios = servicios.__len__()
        print(cont_servicios)  

        return render(request, "Principal/index.html",{"tarjeta_gasto_total":suma, "tarjeta_gasto_color":color_tarj_gastos, "tarjeta_servicio_cantidad":cont_servicios, "tabla_servicios":servicios, "tarjeta_insumo_color":color_tarj_insumo, "tarjeta_insumo_cantidad":cont_insumos})

    return render(request, "Principal/index.html")

def insumo_todos(request):    
    if request.method == "GET":
        
        insumos =  Insumo.objects.all()       
        contador = insumos.__len__()
               
        return render(request, "Principal/insumo_todos.html",{"insumos":insumos, "contador":contador})

def insumo_formulario(request):
    if request.method == "POST":
        mi_form = InsumoFormulario(request.POST) #Aqui me llega la info del html
       
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            stock = Stock(st_actual = info["insumo_stock_actual"],
                          st_minimo = info["insumo_stock_minimo"],
                          st_maximo = info["insumo_stock_maximo"])        
            stock.save()

            insumo = Insumo(ins_codigo = info["insumo_codigo"],
                            ins_nombre = info["insumo_nombre"], 
                            ins_marca = info["insumo_marca"],
                            ins_descripcion = info["insumo_descripcion"],                             
                            ins_unidad_medida = info["insumo_unidad"],
                            ins_contenido = info["insumo_contenido"],
                            ins_stock = stock)
            insumo.save()   

            mi_form = InsumoFormulario()
            return render(request, "Principal/insumo_agregar.html", {"mi_formulario":mi_form})
    else:
        mi_form = InsumoFormulario()
        
    return render(request, "Principal/insumo_agregar.html", {"mi_formulario":mi_form})