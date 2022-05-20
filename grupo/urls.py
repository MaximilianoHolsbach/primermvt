from django.urls import path
from grupo import views

#Recivimos la redirecc de grupo/
#si yo recibo una request localhost:8000/grupo/agregar : django va a ir primero al archivo 
#url del mvtandresholsbach y va a buscar algo que empiece con grupo.
#de alli va a ir a grupo.urls va a buscar la siguiente parte de la ruta. Cuando la encuentre
#se a ir a views dentro de la app grupo.

urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar")
]
