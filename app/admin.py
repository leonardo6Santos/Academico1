from django.contrib import admin
from .models import *   # Importa todos os models de uma vez

# Registro simples (mais fácil de testar)
admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Turno)
admin.site.register(Turma)
admin.site.register(AvaliacaoTipo)
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)