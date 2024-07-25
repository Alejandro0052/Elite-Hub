from django.db import models
from Deportista.models import Deportista

class Deporte(models.Model):
    deportista = models.OneToOneField(Deportista, related_name='deporte_detail',  on_delete=models.CASCADE, primary_key=True)
    deporte_que_practica = models.CharField(max_length=45)
  #  nombre = models.CharField(max_length=50)
    descripcion = models.TextField()