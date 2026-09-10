from rest_framework import serializers
from .models import Quadra, Reserva

class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__' # Inclui todos os campos do modelo


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__' 