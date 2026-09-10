from django.shortcuts import render

from .models import Quadra
from .serializers import QuadraSerializer

from rest_framework.views import APIView # Cria a View da API
from rest_framework.response import Response # Envia uma resposta para o cliente
from rest_framework import status # Códigos HTTP (200, 201, 404...)

class QuadraListCreateView(APIView):
    def get(self, request):
        """Busca e retorna todas as quadras em JSON."""

        quadras = Quadra.objects.all()
        serializer = QuadraSerializer(quadras, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Valida e salva uma nova quadra."""
        serializer = QuadraSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST)