from django.urls import path, patterns, include
from . import views





urlpatterns = [

    path('', views.login, name='index_login'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path(r'^search/$', views.search, name='search'),







]
