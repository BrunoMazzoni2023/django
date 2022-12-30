"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import principal
from home.views import inicio
from home.views import login
from home.views import cadastro
from home.views import dashboard
from home.views import logout
from home.views import home, form, create, view, edit, update, delete
from home.views import homeproduto, formproduto, createproduto, viewproduto, editproduto, updateproduto, deleteproduto
from home.views import homevenda, formvenda, createvenda, viewvenda, editvenda, updatevenda, deletevenda
from home.views import homeestoque4peca, formestoque4peca, createestoque4peca, viewestoque4peca, editestoque4peca, updateestoque4peca, deleteestoque4peca
from home.views import homeestoque1peca, formestoque1peca, createestoque1peca, viewestoque1peca, editestoque1peca, updateestoque1peca, deleteestoque1peca
from django.contrib import messages, auth
#from home.views import login, logout, index, cadastro, dashboard
from django.contrib.auth.decorators import login_required
#from home.views import search
#from home.views import searchpessoa
#from home.views import searchproduto


urlpatterns = [
   # path('', include('home.urls')),  USAR ESTE MODO COMBINANDO COM O URLS APARTE


    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('principal/', principal, name='principal'),
#da ma              path('search/',search, name='search'),
#     path('searchpessoa/',searchpessoa, name='searchpessoa'),
#    path('searchproduto/',searchproduto, name='searchproduto'),




                  # URLS CLIENTES
    path('homepessoa/', home, name='home'),
    path('formpessoa/', form, name='form'),
    path('createpessoa/', create, name='create'),
    path('viewpessoa/<int:pk>/', view, name='view'),
    path('editpessoa/<int:pk>/', edit, name='edit'),
    path('updatepessoa/<int:pk>/', update, name='update'),
    path('deletepessoa/<int:pk>/', delete, name='delete'),



                  # URLS PRODUTOS
     path('homeproduto/', homeproduto, name='homeproduto'),
     path('formproduto/', formproduto, name='formproduto'),
     path('createproduto/', createproduto, name='createproduto'),
     path('viewproduto/<int:pk>/', viewproduto, name='viewproduto'),
     path('editproduto/<int:pk>/', editproduto, name='editproduto'),
     path('updateproduto/<int:pk>/', updateproduto, name='updateproduto'),
     path('deleteproduto/<int:pk>/', deleteproduto, name='deleteproduto'),

                # URLS VENDA
     path('homevenda/', homevenda, name='homevenda'),
     path('formvenda/', formvenda, name='formvenda'),
     path('createvenda/', createvenda, name='createvenda'),
     path('viewvenda/<int:pk>/', viewvenda, name='viewvenda'),
     path('editvenda/<int:pk>/', editvenda, name='editvenda'),
     path('updatevenda/<int:pk>/', updatevenda, name='updatevenda'),
     path('deletevenda/<int:pk>/', deletevenda, name='deletevenda'),

                # URLS ESTOQUE 4 PEÇA

    path('homeestoque4peca/', homeestoque4peca, name='homeestoque4peca'),
    path('formestoque4peca/', formestoque4peca, name='formestoque4peca'),
    path('createestoque4peca/', createestoque4peca, name='createestoque4peca'),
    path('viewestoque4peca/<int:pk>/', viewestoque4peca, name='viewestoque4peca'),
    path('editestoque4peca/<int:pk>/', editestoque4peca, name='editestoque4peca'),
    path('updateestoque4peca/<int:pk>/', updateestoque4peca, name='updateestoque4peca'),
    path('deleteestoque4peca/<int:pk>/', deleteestoque4peca, name='deleteestoque4peca'),

                # URLS ESTOQUE 1 PEÇA

    path('homeestoque1peca/', homeestoque1peca, name='homeestoque1peca'),
    path('formestoque1peca/', formestoque1peca, name='formestoque1peca'),
    path('createestoque1peca/', createestoque1peca, name='createestoque1peca'),
    path('viewestoque1peca/<int:pk>/', viewestoque1peca, name='viewestoque1peca'),
    path('editestoque1peca/<int:pk>/', editestoque1peca, name='editestoque1peca'),
    path('updateestoque1peca/<int:pk>/', updateestoque1peca, name='updateestoque1peca'),
    path('deleteestoque1peca/<int:pk>/', deleteestoque1peca, name='deleteestoque1peca'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)