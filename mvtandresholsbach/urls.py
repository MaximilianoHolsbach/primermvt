"""mvtandresholsbach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Esto es el proyecto django por aca van a ingresar las concultas
#y seran redirigidas a la app en este caso grupo.
from django.contrib import admin
from django.urls import path, include

#importo include, y coloco como argumento el nombre de la carpeta.el archivo urls

urlpatterns = [
    path('grupo/', include('grupo.urls')),
    path('admin/', admin.site.urls),
]

#todo lo que sea grupo/ va a ser redirecc a grupo.urls