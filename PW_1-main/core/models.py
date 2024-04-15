from django.db import models

class PDF(models.Model):
    nombre = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    objetivos = models.TextField(null=True, blank=True)#Para textos largos como fundamentos, bibliografia, etc
    fundamentacion = models.TextField(null=True, blank=True) 
    contenido = models.TextField(null=True, blank=True)
    metodologia = models.TextField(null=True, blank=True)
    evaluacion = models.TextField(null=True, blank=True)
    bibliografia = models.TextField()



    def __str__(self):
        return self.archivo

 