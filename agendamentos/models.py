from django.db import models
from django.contrib.auth.models import User

class Quadra(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    preco_hora = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço hora')

    class Meta:
        verbose_name_plural = 'Quadras'

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    quadra = models.ForeignKey(Quadra, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)
    horario_inicio = models.DateTimeField()
    horario_fim = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Reservas'
        ordering = ['-horario_inicio']

    def __str__(self):
        return f'{self.quadra} - {self.horario_inicio.strftime("%d/%m/%Y %H:%M")}'