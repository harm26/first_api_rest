from django.db import models

COLORES = (
    ('0', 'blanco'),
    ('1', 'negro'),
    ('2', 'rojo'),
    ('3', 'azul'),
    ('4', 'amarillo'),
)

class Deposito(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)

# Create your models here.


class Articulo (models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=2, choices = COLORES)
    deposito = models.ForeignKey(Deposito, null=True, blank=True, on_delete = models.SET_NULL)


