from django.shortcuts import render

from .models import Publicacao, Utilizador


def home(request):
    total_utilizadores = Utilizador.objects.count()
    total_publicacoes = Publicacao.objects.count()
    ultimas_publicacoes = Publicacao.objects.select_related('autor').order_by('-criado_em')[:5]

    context = {
        'total_utilizadores': total_utilizadores,
        'total_publicacoes': total_publicacoes,
        'ultimas_publicacoes': ultimas_publicacoes,
    }
    return render(request, 'main/home.html', context)


def publicacoes(request):
    lista_publicacoes = Publicacao.objects.select_related('autor').prefetch_related('comentarios').order_by('-criado_em')
    return render(request, 'main/publicacoes.html', {'publicacoes': lista_publicacoes})


def utilizadores(request):
    lista_utilizadores = Utilizador.objects.prefetch_related('publicacoes').order_by('nome')
    return render(request, 'main/utilizadores.html', {'utilizadores': lista_utilizadores})
