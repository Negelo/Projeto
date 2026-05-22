from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def publicacoes(request):
    return render(request, 'main/publicacoes.html')


def utilizadores(request):
    return render(request, 'main/utilizadores.html')
