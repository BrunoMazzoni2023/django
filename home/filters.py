from django.contrib.auth.models import User
from home.models import Pessoa
from home.models import Produto
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']




class PessoaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Pessoa
        fields = ['nome']




class ProdutoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    carro = django_filters.CharFilter(lookup_expr='icontains')



    class Meta:
        model = Produto
        fields = ('nome','carro')

