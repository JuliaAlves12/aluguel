from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from rest_framework.decorators import api_view
from .serializers import UsuarioSerializer, ImovelSerializer, ContratoSerializer, PagamentoSerializer


# GET e POST
class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# UPDATE e DELETE
class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# GET e POST
@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':
        queryset = Usuario.objects.all()
        serializers = UsuarioSerializer(queryset, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = UsuarioSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


#Começando sozinha
# Imovel
class ImovelListCreateAPIView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ImovelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    
@api_view(['Get', 'POST'])
def listar_imovel(request):
    if request.method == 'GET':
        queryset = Imovel.objects.all()
        serializers = ImovelSerializer(queryset, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = ImovelSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Contrato
class ContratoListCreateAPIView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
@api_view(['Get', 'POST'])
def listar_contrato(request):
    if request.method == 'GET':
        queryset = Contrato.objects.all()
        serializers = ContratoSerializer(queryset, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = ContratoSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Pagamento
class PagamentoListCreateAPIView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    
@api_view(['Get', 'POST'])
def listar_pagamento(request):
    if request.method == 'GET':
        queryset = Pagamento.objects.all()
        serializers = PagamentoSerializer(queryset, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = PagamentoSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
############################ Via APIView #################################