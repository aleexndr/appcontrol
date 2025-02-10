from django.db import models

# Create your models here.

class Alimentos(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre