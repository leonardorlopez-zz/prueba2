from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()

    
