from django.db import models

class Compras(models.Model):
    nombre = models.CharField(max_length=25)
    codigo = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.codigo}" 
    