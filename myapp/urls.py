from django.urls import path
from . import views

urlpatterns = [
path( "" , views.index, name = "index" ), 
path("cursos", views.cursos, name="cursos"),
path("nuevo-curso", views.nuevo_curso, name="nuevo_curso"),
path("cursos-json", views.cursos_json, name="cursos_json"),
path("curso", views.curso, name="curso"),
]
