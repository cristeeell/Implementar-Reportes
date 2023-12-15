"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path

"""
from django.contrib import admin
from django.urls import path
from webapp.views import jugadores
from jugadores.views import agregar_jugador, modificar_jugador, ver_jugador, eliminar_jugador, generar_reporte

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jugadores, name='jugadores'),
    path('agregar_jugador/', agregar_jugador, name='agregar_jugador'),
    path('modificar_jugador/<int:jugador_id>/', modificar_jugador, name='modificar_jugador'),
    path('ver_jugador/<int:jugador_id>/', ver_jugador, name='ver_jugador'),
    path('eliminar_jugador/<int:jugador_id>/', eliminar_jugador, name='eliminar_jugador'),
    path('generar_reporte/', generar_reporte)
]


