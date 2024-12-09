from django.urls import path
from app import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('calendario', views.calendario, name='calendario'),
    path('noticias', views.noticias, name='noticias'),
    path('contacto', views.contacto, name='contacto'),
    path('tabla', views.tabla, name='tabla'),
    path('equipos', views.equipos, name='equipos'),
    path('galeria', views.galeria, name='galeria'),
    path('terceraA', views.terceraA, name='terceraA'),
    path('norte', views.norte, name='norte'),
    path('centro', views.centro, name='centro'),
    path('sur', views.sur, name='sur'),
]
