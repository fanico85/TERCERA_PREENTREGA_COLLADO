from django import forms

class ServicioFormulario(forms.Form):
    servicio_nombre = forms.CharField(max_length=30,label="Servicio")
    servicio_descripcion = forms.CharField(max_length=100,label="Descripción")
    servicio_duracion = forms.IntegerField(min_value=10,max_value=120,label="Duración")

class ServicioBuscar(forms.Form):
    servicio_nombre = forms.CharField(max_length=30, label="Servicio") #required=False -> para que no sea obligatorio el campo 

class GastoFormulario(forms.Form):
    gasto_nombre = forms.CharField(max_length=50,label="Gasto")
    gasto_descripcion = forms.CharField(max_length=100,label="Descripción")
    gasto_monto = forms.DecimalField(decimal_places=2, max_digits=10, label="Monto",label_suffix=": $")
    gasto_fecha = forms.DateField(label="Fecha (DD/MM/AAAA)")

class InsumoFormulario(forms.Form):
    insumo_codigo = forms.CharField(max_length=20,label="Codigo")
    insumo_nombre = forms.CharField(max_length=50,label="Nombre")
    insumo_descripcion = forms.CharField(max_length=100,label="Descripción")
    insumo_marca = forms.CharField(max_length=50,label="Marca")
    insumo_unidad = forms.CharField(max_length=20,label="Unidad de medida")
    insumo_contenido = forms.IntegerField(min_value=1, label="Contenido")
    insumo_stock_actual = forms.IntegerField(max_value=100, min_value=0, label="Stock inicial")
    insumo_stock_minimo = forms.IntegerField(max_value=100, min_value=0, label="Stock minimo")
    insumo_stock_maximo = forms.IntegerField(max_value=100, min_value=0, label="Stock maximo")
