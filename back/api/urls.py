from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'imoveis', ImovelViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'pagamentos', PagamentoViewSet)

urlpatterns = [
    # path('usuarios', UsuarioListCreateAPIView.as_view()),
    # path('usuario/<int:pk>', UsuarioDetailView.as_view()),

    path('users', listar_usuarios, name="listar_usuarios"),

    path('', include(router.urls)),
    
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
 
    # path('imoveis', ImovelListCreateAPIView.as_view()),
    # path('imovel/<int:pk>', ImovelDetailView.as_view()),
    # path('property', listar_imovel),

    # path('contratos', ContratoListCreateAPIView.as_view()),
    # path('contrato/<int:pk>', ContratoDetailView.as_view()),
    # path('contracts', listar_contrato),

    # path('pagamentos', PagamentoListCreateAPIView.as_view()),
    # path('pagamento/<int:pk>',PagamentoDetailView.as_view()),
    # path('payments', listar_pagamento),
]


