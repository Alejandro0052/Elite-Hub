from django.db import models
from Usuarios.models import Usuario



class Deportista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deporte = models.CharField(max_length=25)
    edad = models.ImageField()

    def __str__(self):
        return f'{self.usuario.nombre} - {self.deporte}'