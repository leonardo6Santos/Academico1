from django.contrib import admin
from django.urls import path
from app import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('instituicoes/', views.lista_instituicoes, name='lista_instituicoes'),
    path('cidades/', views.lista_cidades, name='lista_cidades'),
    path('ocorrencias/', views.lista_ocorrencias, name='lista_ocorrencias'),
]