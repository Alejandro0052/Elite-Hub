from django.db import models
from Usuarios.models import Usuario
from Deporte.models import Deporte


class Patrocinador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCAD)
    descripcion = models.CharField(max_length=20)
   # nombre = models.CharField(max_length=20)
    #apellido = models.CharField(max_length=20)
    #numero_telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}' 