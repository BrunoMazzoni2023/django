from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db.models import Count
from django.db.models import Max, Min
from datetime import datetime, date


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    endereco = models.CharField(max_length=120)
    complemento = models.CharField(max_length=120)
    cep =  models.CharField(max_length=12)
    telefone = models.CharField(max_length=12)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    produto = models.CharField(max_length=128)
    vendas = models.ManyToManyField(Pessoa, through='Venda')
    obs = models.TextField(blank=True)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.produto

PAGAMENTO = (
    ('Em atendimento', 'Em atendimento'),
    ('A Vista', 'A Vista'),
    ('Pago', 'Pago'),
    ('A Prazo', 'A Prazo'),
    ('Orçamento', 'Orçamento'),
    ('Vencido', 'Vencido'),
    ('Parcelado 3X', 'Parcelado 3X')

)
class Venda(models.Model):
    titulo = models.CharField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    placa = models.CharField(max_length=128)
    carro = models.CharField(max_length=128)
    data_venda = models.DateTimeField(default=timezone.now)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    venc_fatura = models.DateField(blank=True, null=True)
    obs = models.TextField(max_length=100)
    pag = models.CharField(max_length=20, choices=PAGAMENTO)

def __str__(self):
        return self.titulo







class Estoque4peca(models.Model):
    produto = models.CharField(max_length=120)
    motorista = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    passageiro = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    assento_esquerdo = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    assento_direito = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    quantidade_em_estoque = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    estoque_minimo = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    obs = models.TextField(blank=True)

    def __str__(self, ):
        return self.produto


class Estoque1peca(models.Model):
    produto = models.CharField(max_length=110)
    quantidade_em_estoque = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    estoque_minimo = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    obs = models.TextField(blank=True)

    def __str__(self, ):
        return self.produto



