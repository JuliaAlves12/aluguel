from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

######################### VIA MODEL VIEW SET #############################

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo') #olha todos os usuarios pelo tipo
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)
    #     return self.queryset

    filter_backends = [DjangoFilterBackend] # para dizer que ta usando os filters
    filterset_class = UsuarioFilter

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo') #primeiro coleta os parametros
    #     status = self.request.query_params.get('status')

    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo) # faz os if's

    #     if status:
    #         self.queryset = self.queryset.filter(status=status)
            
    #     return self.queryset #retorna fora dos if's, se não ele não entende

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer


# GENERICS (Mais Fácil)

# GET e POST
# class UsuarioListCreateAPIView(ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # UPDATE e DELETE
# class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer



############################ Via Método ############################ 
######################### Somente @api_view ########################


# Via API VIEW (Com mais métodos)

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


# GENERICS (Mais Fácil)

#Começando sozinha
# Imovel
# class ImovelListCreateAPIView(ListCreateAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# class ImovelDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer
    


# Via API VIEW (Com mais métodos)

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
    

# GENERICS (Mais Fácil)

# Contrato
# class ContratoListCreateAPIView(ListCreateAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer

# class ContratoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer
    


# Via API VIEW (Com mais métodos)

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
    

# GENERICS (Mais Fácil)

# Pagamento
# class PagamentoListCreateAPIView(ListCreateAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer

# class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer
    


# Via API VIEW (Com mais métodos)

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

############################ USUARIO #####################################

# class UsuarioListCreateAPIView(APIView):

#     def get(self, request): # GET
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)
    
#     def post(self, request): # POST
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
# class UsuarioDetailView(APIView):

#     def get_object(self, pk): #USADO PARA CRIAR PUT E DELETE
#         return Usuario.objects.get(pk=pk) 
    
#     def get(self, request, pk): 
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario)
#         return Response(serializer.data)
    
#     def delete(self, request, pk): # DELETE
#         usuario = self.get_object(pk)
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk): # PUT
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# ##################################### IMOVEIS ###########################################

# class ImovelListCreateAPIView(APIView):

#     def get(self, request): # GET
#         imoveis = Imovel.objects.all()
#         serializer = ImovelSerializer(imoveis, many=True)
#         return Response(serializer.data)
    
#     def post(self, request): # POST
#         serializer = ImovelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
# class ImovelDetailView(APIView):

#     def get_object(self, pk): #USADO PARA CRIAR PUT E DELETE
#         return Imovel.objects.get(pk=pk) 
    
#     def get(self, request, pk): 
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel)
#         return Response(serializer.data)
    
#     def delete(self, request, pk): # DELETE
#         imovel = self.get_object(pk)
#         imovel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk): # PUT
#         imovel = self.get_object(pk)
#         serializer =ImovelSerializer(imovel, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ##################################### CONTRATO ###########################################

# class ContratoListCreateAPIView(APIView):

#     def get(self, request): # GET
#         contratos = Contrato.objects.all()
#         serializer = ContratoSerializer(contratos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request): # POST
#         serializer = ContratoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# class ContratoDetailView(APIView):

#     def get_object(self, pk): #USADO PARA CRIAR PUT E DELETE
#         return Contrato.objects.get(pk=pk) 
    
#     def get(self, request, pk): 
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato)
#         return Response(serializer.data)
    
#     def delete(self, request, pk): # DELETE
#         contrato = self.get_object(pk)
#         contrato.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk): # PUT
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ##################################### PAGAMENTO ###########################################

# class PagamentoListCreateAPIView(APIView):

#     def get(self, request): # GET
#         pagamentos = Pagamento.objects.all()
#         serializer = PagamentoSerializer(pagamentos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request): # POST
#         serializer =PagamentoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# class PagamentoDetailView(APIView):

#     def get_object(self, pk): #USADO PARA CRIAR PUT E DELETE
#         return Pagamento.objects.get(pk=pk) 
    
#     def get(self, request, pk): 
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento)
#         return Response(serializer.data)
    
#     def delete(self, request, pk): # DELETE
#         pagamento = self.get_object(pk)
#         pagamento.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk): # PUT
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

