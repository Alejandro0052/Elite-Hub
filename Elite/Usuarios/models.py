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
    


class Pqrs(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.asunto}'
    


class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
    #patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
   # marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.texto}'
    

class Contenido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
   # deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
    #patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    #marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.titulo}'