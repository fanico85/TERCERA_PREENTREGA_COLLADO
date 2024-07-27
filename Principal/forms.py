from django import forms

class ServicioFormulario(forms.Form):
    nombre_servicio= forms.CharField()
    descripcion = forms.CharField()