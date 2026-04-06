from django.shortcuts import render
from .models import Pessoa, Curso, InstituicaoEnsino, Cidade, Ocorrencia

def index(request):
    return render(request, 'index.html')

def lista_pessoas(request):
    
    context = {'pessoas': Pessoa.objects.all()}
    return render(request, 'pessoas.html', context)

def lista_cursos(request):
    
    context = {'cursos': Curso.objects.all()}
    return render(request, 'cursos.html', context)

def lista_instituicoes(request):
    
    context = {'instituicoes': InstituicaoEnsino.objects.all()}
    return render(request, 'instituicoes.html', context)

def lista_cidades(request):

    context = {'cidades': Cidade.objects.all()}
    return render(request, 'cidades.html', context)

def lista_ocorrencias(request):
  
    context = {'ocorrencias': Ocorrencia.objects.all()}
    return render(request, 'ocorrencias.html', context)