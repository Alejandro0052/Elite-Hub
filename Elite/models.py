from django.db import models


class Usuario(models.Model):
    descripcion = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero_telefono = models.IntegerField()
    correo = models.CharField(max_length=80)
    fecha_registro = models.DateField()
    direccion = models.CharField(max_length=20)
    edad = models.IntegerField()
    

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Deportista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deporte = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.usuario.nombre} - {self.deporte}'