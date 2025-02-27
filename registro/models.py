from django.db import models

# Create your models here.

class Alimentos(models.Model):
    preciokg_alimentos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    producto_alimentos = models.CharField(max_length=255, blank=True)
    cantidad_alimentos = models.CharField(max_length=255, blank=True)
    costo_alimentos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_alimentos = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.producto_alimentos
    
class Transporte(models.Model):
    OPCIONES_TRANSPORTE = [
        ('Gas', 'Gas'),
        ('Combustible', 'Combustible'),
        ('Pasaje', 'Pasaje'),
    ]

    opcion_transporte = models.CharField(max_length=20, choices=OPCIONES_TRANSPORTE, blank=True)
    tipo_transporte = models.CharField(max_length=255, blank=True)
    cantidad_transporte = models.CharField(max_length=255, blank=True)
    costo_transporte = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_transporte = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.opcion_transporte} - {self.tipo_transporte}"
    
class Servicios(models.Model):
    nombre_servicios = models.CharField(max_length=255, blank=True)
    tipo_servicios = models.CharField(max_length=255, blank=True)
    costo_servicios = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_servicios = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_servicios