from django.contrib import admin
from.models import Pessoa, Produto, Venda,Estoque4peca,Estoque1peca

class ListandoPessoa(admin.ModelAdmin):
    list_display = ('id', 'nome','endereco','complemento','cep','telefone','observacao')
    list_display_links = ('nome'),
    list_filter = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class ListandoProduto(admin.ModelAdmin):
    list_display = ('id', 'produto','obs')
    list_display_links = ('produto'),
    list_filter = ('produto',)
    list_per_page = 10
    search_fields = ('produto',)


class ListandoVenda(admin.ModelAdmin):
    list_display = ('id', 'titulo','pessoa','produto','placa','carro')

    list_display_links = ('id', 'titulo','pessoa',)
    list_filter =  ('id', 'titulo','pessoa','produto','placa','carro')
    list_per_page = 3
    search_fields = ('id', 'titulo','pessoa__nome','produto__produto','placa','carro','obs')
    readonly_fields = ('id',)



admin.site.register(Pessoa, ListandoPessoa)
admin.site.register(Produto, ListandoProduto)
admin.site.register(Venda, ListandoVenda)
admin.site.register(Estoque4peca)
admin.site.register(Estoque1peca)

