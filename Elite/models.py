from django.db import models

class Usuario(models.Model):
    descripcion = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    numero_telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=80)
    fecha_registro = models.DateField()
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField()
    

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Nutricionista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    especialidad = models.CharField(max_length=40)

   
    def __str__(self):
        return f'{self.especialidad}'
    


class Deportista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deporte = models.CharField(max_length=25)
   # edad = models.IntegerField()

    def __str__(self):
        return f'{self.deporte}'
    
class Patrocinador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    #descripcion = models.CharField(max_length=20)
   # nombre = models.CharField(max_length=20)
    #apellido = models.CharField(max_length=20)
    #numero_telefono = models.IntegerField()
    deportistas_interes = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.deportistas_interes}' 
    
    
class Marca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #descripcion = models.CharField(max_length=20)
    #nombre = models.CharField(max_length=20)
    #apellido = models.CharField(max_length=20)
    #numero_telefono = models.IntegerField()
    #razon_social = models.CharField(max_length=60)
    razon_social = models.CharField(max_length=60, default='Valor Predeterminado')

    def __str__(self):
        return f'{self.razon_social}'

#PENDIENTE DE DISEÑAR BIEN COMO SE VA A MANEJAR ESTE TEMA DE LOS INVITADOS QUE NO VAN A TENER CREADO UN PERFIL
class Invitados(models.Model):
  # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    descripcion = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero_telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.descripcion}'


class Pqrs(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.asunto}'


class Comentarios(models.Model):
    deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
    patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.texto}'

#Agregue related_name='deporte_detail'
class Deporte(models.Model):
    deportista = models.OneToOneField(Deportista, related_name='deporte_detail',  on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre}'


class Contenido(models.Model):
    deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
    patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.titulo}'
    

##Another superclass, it is not yet related to more classes, (they are only related to those below)

class Facturacion(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    numero_factura = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    Valor_factura = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre_usuario}'



class EncabezadoFact(models.Model):
    facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    resolucion_fact = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre_usuario}'


class DetalleFact(models.Model):
    facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_usuario = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre_usuario}'


class Pagos(models.Model): 
      facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
      valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
      fecha_pago =  models.DateField()
      nombre_usuario = models.CharField(max_length=30)

      def __str__(self):
        return f'{self.nombre_usuario}'




   