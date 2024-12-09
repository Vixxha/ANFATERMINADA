from django.shortcuts import render
from app.models import Equipos, Noticia, Partido, TerceraA, Norte, Centro, Sur, Programados

# Create your views here.

def index(request):
    partidos_programados = Programados.objects.all()
    return render(request, 'web/index.html', {'partidos_programados': partidos_programados})


def calendario(request):
    partidos = Partido.objects.filter(fecha__month=3)
    partidos_tercera_a = Partido.objects.filter(zona='Tercera A', fecha__month=3)
    partidos_norte = Partido.objects.filter(zona='Norte', fecha__month=3)
    partidos_centro = Partido.objects.filter(zona='Centro', fecha__month=3)  # Filtrar partidos de la zona Centro
    partidos_sur = Partido.objects.filter(zona='Sur', fecha__month=3)  # Filtrar partidos de la zona Sur
    return render(request, 'web/calendario.html', {'partidos': partidos, 'partidos_tercera_a': partidos_tercera_a, 'partidos_norte': partidos_norte, 'partidos_centro': partidos_centro, 'partidos_sur': partidos_sur})


def partidos_tercera_a(request):
    partidos_tercera_a = Partido.objects.filter(zona='Tercera A', fecha__month=3)
    return render(request, 'web/calendario.html', {'partidos': partidos_tercera_a})

def partidos_norte(request):
    partidos_norte = Partido.objects.filter(zona='Norte', fecha__month=3)
    return render(request, 'web/calendario.html', {'partidos': partidos_norte})

def partidos_centro(request):
    partidos_centro = Partido.objects.filter(zona='Centro', fecha__month=3)
    return render(request, 'web/calendario.html', {'partidos': partidos_centro})

def partidos_sur(request):
    partidos_sur = Partido.objects.filter(zona='Sur', fecha__month=3)
    return render(request, 'web/calendario.html', {'partidos': partidos_sur})

def noticias(request):
    try:
        noticias = Noticia.objects.all()
    except Exception as e:
        noticias = []

    context = {
        'noticias': noticias
    }
    return render(request, 'web/noticias.html', context)

def contacto(request):
    return render(request, 'web/contacto.html')

def tabla(request):
    try:
        equipos = Equipos.objects.all().order_by('-puntos')
    except Exception as e:
        equipos = []

    context = {
        'equipos': equipos
    }
    return render(request, 'web/tabla.html', context)


def equipos(request):
    equipos = Equipos.objects.all()

    data = {
        'equipos': equipos
    }
    return render(request, 'web/equipos.html', data)

def galeria(request):
    return render(request, 'web/galeria.html')

def terceraA(request):
    equipos_tercera_a = TerceraA.objects.all().order_by('-puntos')
    context = {'equipos_tercera_a': equipos_tercera_a}
    return render(request, 'web/terceraA.html', context)

def norte(request):
    equipos_norte = Norte.objects.all().order_by('-puntos')
    context = {'equipos_norte': equipos_norte}
    return render(request, 'web/norte.html', context)

def centro(request):
    equipos_centro = Centro.objects.all().order_by('-puntos')
    context = {'equipos_centro': equipos_centro}
    return render(request, 'web/centro.html', context)

def sur(request):
    equipos_sur = Sur.objects.all().order_by('-puntos')
    context = {'equipos_sur': equipos_sur}
    return render(request, 'web/sur.html', context)