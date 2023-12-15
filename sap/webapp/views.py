# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from jugadores.models import Jugador


def jugadores(request):
    jugadores = Jugador.objects.annotate(num_juegos_preferidos=Count('juego_preferido'))
    cantidad_jugadores = jugadores.count()
    cantidad_juegos_preferidos = sum(1 for jugador in jugadores)
    dict_datos = {
        'cantidad_jugadores': cantidad_jugadores,
        'jugadores': jugadores
    }
    pagina = loader.get_template('jugadores.html')
    return HttpResponse(pagina.render(dict_datos, request))

