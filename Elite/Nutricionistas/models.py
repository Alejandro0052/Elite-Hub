from django.db import models
from Usuarios.models import Usuario

class Nutricionista(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #descripcion = models.CharField(max_length=20)
    #nombre = models.CharField(max_length=20)
    #apellido = models.CharField(max_length=20)
    #numero_telefono = models.IntegerField()
    #correo = models.CharField(max_length=80)
   # fecha_registro = models.DateField()
    #direccion = models.CharField(max_length=20)
    edad = models.IntegerField()
    

    def __str__(self):
        return f'{self.edad}'