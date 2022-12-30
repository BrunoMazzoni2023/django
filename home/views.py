from django.shortcuts import render, redirect
from home.forms import PessoaForm
from home.forms import ProdutoForm
from home.forms import VendaForm
from home.models import Pessoa
from home.models import Produto
from home.models import Venda
from home.forms import Estoque4peca
from home.forms import Estoque4pecaForm
from home.forms import Estoque1peca
from home.forms import Estoque1pecaForm
from django.core.validators import validate_email
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.filters import UserFilter
from home.filters import PessoaFilter
from home.filters import ProdutoFilter
from django.views import generic
from . import forms, models
from django_filters import rest_framework as filters
from django.db.models import Q
from django.core.paginator import Paginator




# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////




#INICIAL VIEWS VIEWS ////////////////////////////////////////////////

def inicio(request):
    return render(request, 'inicio.html')

#PAGINA PRINCIPAL DOS MENUS

def principal(request):
    return render(request, 'principal.html')

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

#PESSOA  VIEWS VIEWS ////////////////////////////////////////////////
#PESSOA  VIEWS VIEWS ////////////////////////////////////////////////
#PESSOA  VIEWS VIEWS ////////////////////////////////////////////////

#  FILTRO VIEWS  PESSOA ////////////////////////////////////////////////


def home(request):
    data = {}
    data['db'] = Pessoa.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']

        data = Pessoa.objects.filter(nome__icontains=q )
        multiple_q = Q(Q(nome__icontains=q) | Q(endereco__icontains=q))
        data = Pessoa.objects.filter(multiple_q)

    else:
        data = Pessoa.objects.all()
    context = {
        'data' : data,
    }

    paginator = Paginator(data, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pessoa/index.html', {'data': page_obj})


    return render(request, 'pessoa/index.html', context)



def form(request):
    data = {}
    data ['form'] = PessoaForm()
    return render(request, 'pessoa/formpessoa.html', data)


def create(request):
    form = PessoaForm(request.POST or None)

    if form.is_valid():
        form.save()
    messages.success(request, 'Cliente Cadastrado Com Sucesso.')
    return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request, 'pessoa/viewpessoa.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    data['form'] = PessoaForm(instance=data['db'])
    return render(request, 'pessoa/formpessoa.html', data)

def update(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home')



#PRODUTO VIEWS VIEWS ////////////////////////////////////////////////
#PRODUTO VIEWS VIEWS ////////////////////////////////////////////////
#PRODUTO VIEWS VIEWS ////////////////////////////////////////////////

#  FILTRO VIEWS  PRODUTO ////////////////////////////////////////////////

def homeproduto(request):
    data = {}
    data['db'] = Produto.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        #data = Produto.objects.filter(nome__icontains=q)
        multiple_q = Q(Q(produto__icontains=q) | Q(obs__icontains=q))
        data = Produto.objects.filter(multiple_q)

    else:
        data = Produto.objects.all()
    context = {
        'data' : data
    }
    return render(request, 'produto/index.html', context)



###############################################################################################
def formproduto(request):
    data = {}
    data ['form'] = ProdutoForm()
    return render(request, 'produto/formproduto.html', data)



def createproduto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('homeproduto')


def viewproduto(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'produto/viewproduto.html', data)

def editproduto(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'produto/formproduto.html', data)

def updateproduto(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('homeproduto')

def deleteproduto(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('homeproduto')


#VENDA VIEWS VIEWS ////////////////////////////////////////////////
#VENDA VIEWS VIEWS ////////////////////////////////////////////////
#VENDA VIEWS VIEWS ////////////////////////////////////////////////


def homevenda(request):
    data = {}
    data['db'] = Venda.objects.all()


    if 'q' in request.GET:
        q = request.GET['q']
        data = Venda.objects.filter(placa__icontains=q)
        multiple_q = Q(Q(placa__icontains=q) | Q(carro__icontains=q) | Q(pessoa__nome__icontains=q))
        data = Venda.objects.filter(multiple_q)

    else:
        data = Venda.objects.all()

    context = {
        'data' : data,

    }
    return render(request, 'venda/index.html',  context)



def formvenda(request):
    data = {}
    data ['form'] = VendaForm()
    return render(request, 'venda/formvenda.html', data)

def createvenda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('homevenda')

def viewvenda(request, pk):
    data = {}
    data['db'] = Venda.objects.get(pk=pk)
    return render(request, 'venda/viewvenda.html', data)

def editvenda(request, pk):
    data = {}
    data['db'] = Venda.objects.get(pk=pk)
    data['form'] = VendaForm(instance=data['db'])
    return render(request, 'venda/formvenda.html', data)

def updatevenda(request, pk):
    data = {}
    data['db'] = Venda.objects.get(pk=pk)
    form = VendaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('homevenda')

def deletevenda(request, pk):
    db = Venda.objects.get(pk=pk)
    db.delete()
    return redirect('homevenda')

#ESTOQUE 4 PEÇA VIEWS VIEWS ////////////////////////////////////////////////
#ESTOQUE 4 PEÇA  VIEWS VIEWS////////////////////////////////////////////////
#ESTOQUE 4 PEÇA  VIEWS VIEWS////////////////////////////////////////////////

def homeestoque4peca(request):
    data = {}
    data['db'] = Estoque4peca.objects.all()
    return render(request, 'estoque4peca/index.html', data)

def formestoque4peca(request):
    data = {}
    data ['form'] = Estoque4pecaForm()
    return render(request, 'estoque4peca/formestoque4peca.html', data)

def createestoque4peca(request):
    form = Estoque4pecaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('homeestoque4peca')

def viewestoque4peca(request, pk):
    data = {}
    data['db'] = Estoque4peca.objects.get(pk=pk)
    return render(request, 'estoque4peca/viewestoque4peca.html', data)

def editestoque4peca(request, pk):
    data = {}
    data['db'] = Estoque4peca.objects.get(pk=pk)
    data['form'] = Estoque4pecaForm(instance=data['db'])
    return render(request, 'estoque4peca/formestoque4peca.html', data)

def updateestoque4peca(request, pk):
    data = {}
    data['db'] = Estoque4peca.objects.get(pk=pk)
    form = Estoque4pecaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('homeestoque4peca')

def deleteestoque4peca(request, pk):
    db = Estoque4peca.objects.get(pk=pk)
    db.delete()
    return redirect('homeestoque4peca')


#ESTOQUE PARCIAL VIEWS VIEWS ////////////////////////////////////////////////
#ESTOQUE PARCIAL VIEWS VIEWS ////////////////////////////////////////////////
#ESTOQUE PARCIAL VIEWS VIEWS ////////////////////////////////////////////////




def homeestoque1peca(request):
    data = {}
    data['db'] = Estoque1peca.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        data = Estoque1peca.objects.filter(produto__icontains=q)
    else:
        data = Estoque1peca.objects.all()
    context = {
        'data' : data
    }
    return render(request, 'estoque1peca/index.html', context)

def formestoque1peca(request):
    data = {}
    data ['form'] = Estoque1pecaForm()

    return render(request, 'estoque1peca/formestoque1peca.html', data)


def createestoque1peca(request):
    if request.method == 'POST':
        form = Estoque1pecaForm(request.POST)
        if form.is_valid():
            form.save()
    form = Estoque1pecaForm()
    messages.success(request, 'Produto Criado com Sucesso.')
    return redirect('homeestoque1peca')


def viewestoque1peca(request, pk):
    data = {}
    data['db'] = Estoque1peca.objects.get(pk=pk)
    return render(request, 'estoque1peca/viewestoque1peca.html', data)

def editestoque1peca(request, pk):
    data = {}
    data['db'] = Estoque1peca.objects.get(pk=pk)
    data['form'] = Estoque1pecaForm(instance=data['db'])
    return render(request, 'estoque1peca/formestoque1peca.html', data)

def updateestoque1peca(request, pk):
    data = {}
    data['db'] = Estoque1peca.objects.get(pk=pk)
    form = Estoque1pecaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('homeestoque1peca')

def deleteestoque1peca(request, pk):
    db = Estoque1peca.objects.get(pk=pk)
    db.delete()
    return redirect('homeestoque1peca')


#LOGIN VIEWS VIEWS ////////////////////////////////////////////////

def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return redirect( 'login')
    else:
        auth.login(request, user)
        messages.success(request, 'Logado com Sucesso.')
        return redirect('principal')


def logout(request):
    auth.logout(request)
    return render (request,'logout.html')

def cadastro(request):
  if request.method != 'POST':
      return render(request, 'cadastro.html')

  nome = request.POST.get('nome')
  email = request.POST.get('email')
  usuario = request.POST.get('usuario')
  senha = request.POST.get('senha')
  senha2 = request.POST.get('senha2')

  if not nome or not email or not usuario or not senha or not senha2:
      messages.error(request, 'Nenhum campo pode estar vazio.')
      return render(request, 'cadastro.html')

  try:
        validate_email(email)
  except:
        messages.error(request, 'Email Invalido.')
        return render(request, 'cadastro.html')

  if len(senha) < 6:
      messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
      return render(request, 'cadastro.html')

  if senha != senha2:
      messages.error(request, 'Senhas não conferem.')
      return render(request, 'cadastro.html')

  if User.objects.filter(username=usuario).exists():
      messages.error(request, 'Usuário já existe.')
      return render(request, 'cadastro.html')


      messages.error(request, 'Email já existe.')
      return render(request, 'cadastro.html')

  messages.success(request, 'Registrado com sucesso! Agora faça o login.')


  user = User.objects.create_user(username=usuario, email=email,password=senha,first_name=nome)
  user.save()
  return render (request,'login.html')


@login_required(redirect_field_name='login.html')
def dashboard(request):
    return render(request, 'dashboard.html')


