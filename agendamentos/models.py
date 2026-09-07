from django.db import models

class Quadra(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    preco_hora = models.DecimalField(max_digits=10, decimal_places=2)

