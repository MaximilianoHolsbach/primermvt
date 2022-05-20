from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from grupo.forms import personaForm
from grupo.models import persona

def index(request):
    personas = persona.objects.all()
    plantilla = loader.get_template("grupo/index.html")
    context = {
        'personas' : personas,
    }
    return HttpResponse(plantilla.render(context, request))

#Una vez que llegamos del grupo.urls
#Tenemos dos vervos==method posibles GET para mostrar y POST para guardar
#Pero para agregar osea realizar un POST primero debemos realizar un GET.
#Cuando realizo la primer llamada localhost:8000/grupo/agregar: hacemos nuestra primer consulta pero como GET
#XQ estamos solicitando que nos traiga un formulario.
#Cuando le doy guardar al localhost estamos haciendo un POST.

def agregar(request):

    if request.method == "POST":
        form = personaForm(request.POST)# aca tengo una request con un POST con info
        if form.is_valid():#validamos la info del post

            nombre = form.cleaned_data['nombre'] 
            apellido = form.cleaned_data['apellido']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            peso = form.cleaned_data['peso']
            altura = form.cleaned_data['altura']
            email = form.cleaned_data['email']
            persona(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, peso=peso, altura=altura, email=email).save()
            return HttpResponseRedirect("/grupo/")

    elif request.method == "GET":
        form = personaForm()# Aca instanciamos un formulario de persona vacio
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo")#pasmos por alto el else
#simpre que yo pase un diccionario en la funcion render la interpretara como contexto
    return render(request, 'grupo/formcarga.html', {'form':form})# Le solicitamos renderice la vista con un formulario, esto seria el contexto

def borrar(request, identificador):
    if request.method =="GET":
        people = persona.objects.filter(id=int(identificador)).first()
        if people:
            people.delete()
        return HttpResponseRedirect("/grupo/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo")

# Create your views here.
