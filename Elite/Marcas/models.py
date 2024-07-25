from django.db import models
from Usuarios.models import Usuario


class Marca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=45)
    #nombre = models.CharField(max_length=20)
    #apellido = models.CharField(max_length=20)
   # numero_telefono = models.IntegerField()

    
    def __str__(self):
        return f'{self.razon_social} - {self.descripcion}'