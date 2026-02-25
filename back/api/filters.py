import django_filters
from .models import *

class UsuarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains') # procurar se tiver
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='iexact') # Procurar exato

    class Meta:
        model = Usuario
        fields = ['nome', 'tipo']