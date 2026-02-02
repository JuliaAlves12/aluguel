from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import UsuarioSerializer, ImovelSerializer, ContratoSerializer, PagamentoSerializer
# Create your views here.

class UsuarioListCreateAPIView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)