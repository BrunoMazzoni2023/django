from django.forms import ModelForm
from home.models import Pessoa
from home.models import Produto
from home.models import Venda
from home.models import Estoque4peca
from home.models import Estoque1peca
from django.core.exceptions import ValidationError
from django_select2 import forms as s2forms
from . import models

# Create the form class.

# CLIENTE FORM
class PessoaForm(ModelForm):
    class Meta:
     model = Pessoa
     fields = '__all__'



# PRODUTO FORM
class ProdutoForm(ModelForm):
     class Meta:
      model = Produto
      fields = ['produto','obs']

# VENDA FORM

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['titulo', 'pessoa', 'produto', 'placa', 'carro', 'data_venda', 'preco','venc_fatura','obs','pag']


class Estoque4pecaForm(ModelForm):
     class Meta:
      model = Estoque4peca
      fields = ['produto','motorista','passageiro','assento_esquerdo',
                'assento_direito','quantidade_em_estoque', 'estoque_minimo','obs']

class Estoque1pecaForm(ModelForm):
     class Meta:
      model = Estoque1peca
      fields = ['produto','quantidade_em_estoque', 'estoque_minimo', 'obs']


class Estoque1pecaWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "produto__icontains",
        "quantidade_em_estoque__icontains",
    ]
