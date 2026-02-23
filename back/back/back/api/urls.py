from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios', UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>', UsuarioDetailView.as_view()),
    path('users', listar_usuarios),
    path('imoveis', ImovelListCreateAPIView.as_view()),
    path('imovel/<int:pk>', ImovelDetailView.as_view()),
    path('property', listar_imovel),
    path('contratos', ContratoListCreateAPIView.as_view()),
    path('contrato/<int:pk>', ContratoDetailView.as_view()),
    path('contracts', listar_contrato),
    path('pagamentos', PagamentoListCreateAPIView.as_view()),
    path('pagamento/<int:pk>',PagamentoDetailView.as_view()),
    path('payments', listar_pagamento),
]


