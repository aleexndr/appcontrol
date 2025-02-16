from django.db import models

# Create your models here.

class Alimentos(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.CharField(max_length=50, null=True, blank=True)
    preciokg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre