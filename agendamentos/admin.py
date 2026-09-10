from django.contrib import admin
from .models import Quadra, Reserva

@admin.register(Quadra)
class QuadraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    search_fields = ('nome',)
    list_filter = ('tipo',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('quadra', 'usuario', 'horario_inicio', 'horario_fim')
    search_fields = ('qudra__nome', 'usuario__username')