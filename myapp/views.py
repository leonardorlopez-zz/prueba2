import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Curso
from django.http import Http404


def index ( request ):
    ctx = {
        "alumnos": ["Juan", "Sofia", "Matias"]
    }
    return render(request, "myapp/index.html", ctx)

def cursos (request):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)

def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST) #crea una instancia de forms
        if form.is_valid():  #validacion  
            Curso.objects.create(
                nombre = form.cleaned_data["nombre"],
                inscriptos = form.cleaned_data["inscriptos"]
            )
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso()
    ctx = {"form": form}
    return render(request, "myapp/nuevo_curso.html", ctx)
            
   
def cursos_json(request):
    response = JsonResponse(list(Curso.objects.values()), safe=False)
    return response  

def curso(request, nombre):
    try:
        curso = Curso.objects.get(nombre= nombre)
    except Curso.DoesNotExist:
        raise Http404
    ctx = {"curso": curso}
    return render(request, "myapp/curso.html", ctx)

