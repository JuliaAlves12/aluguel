import django_filters
from .models import *

class UsuarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains') # procurar se tiver
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='iexact') # Procurar exato

    class Meta:
        model = Usuario
        fields = ['nome', 'tipo']


class ImovelFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='icontains') # procurar se tiver
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact') # Procurar exato

    class Meta:
        model = Imovel
        fields = ['tipo', 'status']


class ContratoFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='data_inicio', lookup_expr='gte') # gte = valor minimo
    data_fim = django_filters.DateFilter(field_name='data_fim', lookup_expr='lte') # gte = valor minimo
    valor_min = django_filters.NumberFilter(field_name='valor', lookup_expr='gte') # gte = valor minimo
    valor_max = django_filters.NumberFilter(field_name='valor', lookup_expr='lte') # lte = valor máximo

    class Meta:
        model = Contrato
        fields = ['valor_min', 'valor_max', 'data_inicio', 'data_fim']

class PagamentoFilter(django_filters.FilterSet):
    data_pagamento = django_filters.DateFilter(field_name='data_pagamento', lookup_expr='iexact') # Procurar exato
    status = django_filters.BooleanFilter(field_name='status')
    contrato = django_filters.NumberFilter(field_name='contrato_id', lookup_expr='exact')

    class Meta:
        model = Pagamento
        fields = ['data_pagamento', 'status', 'contrato_id']