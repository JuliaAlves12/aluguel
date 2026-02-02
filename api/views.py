from django.shortcuts import render
from rest_framework.response import Response
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import UsuarioSerializer, ImovelSerializer, ContratoSerializer, PagamentoSerializer
from rest_framework.decorators import api_view
# Create your views here.

