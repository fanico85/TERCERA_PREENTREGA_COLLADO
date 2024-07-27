from django import forms

class ServicioFormulario(forms.Form):
    servicio_nombre = forms.CharField(max_length=30,label="Servicio")
    servicio_descripcion = forms.CharField(max_length=100,label="Descripción")
    servicio_duracion = forms.IntegerField(min_value=10,max_value=120,label="Duración")

class GastoFormulario(forms.Form):
    gasto_nombre = forms.CharField(max_length=50,label="Gasto")
    gasto_descripcion = forms.CharField(max_length=100,label="Descripción")
    gasto_monto = forms.DecimalField(decimal_places=2, max_digits=10, label="Monto",label_suffix=": $")
    gasto_fecha = forms.DateField(label="Fecha (MM/DD/AAAA)")

class ServicioBuscar(forms.Form):
    servicio_nombre = forms.CharField(max_length=30, label="Servicio") #required=False -> para que no sea obligatorio el campo 