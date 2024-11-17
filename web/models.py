from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion= models.TextField(null=True)
    precio = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    informacion = models.TextField(null=True)
    imagen = models.ImageField(upload_to='productos')

    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)
       
    def __str__(self):
        return [self.nombre][self.apellido]

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=9,decimal_places=2)
    estado = models.CharField(max_length=200)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT) 
    direccion = models.CharField(max_length=200)







