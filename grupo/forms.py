from django import forms

#forms.py hereda una clase que viene de Forms en el mismo definiremos los campos del formulario

class personaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    fecha_nacimiento = forms.DateField(label="Feha nacimiento", )
    peso = forms.IntegerField(label="Peso", )
    altura = forms.IntegerField(label="Altura", )
    email = forms.CharField(label="Email", max_length=100)