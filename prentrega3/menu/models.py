from django.db import models

class Compras(models.Model):
    nombre = models.CharField(max_length=25)
    codigo = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.codigo} - {self.precio}" 
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=25)
    correo = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.correo} - {self.edad}" 
    
class Distribuidor(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField()
    compañia = models.CharField(max_length=30)
    distributor_numero = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.correo} - {self.compañia} - {self.distributor_numero}"


    