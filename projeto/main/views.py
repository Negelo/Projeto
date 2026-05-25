from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Comentario, Like, Publicacao, Utilizador


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
    if request.method == 'POST':
        acao = request.POST.get('acao')
        publicacao_id = request.POST.get('publicacao_id')
        utilizador_id = request.POST.get('utilizador_id')

        if acao == 'comentar':
            texto = (request.POST.get('texto') or '').strip()
            publicacao = Publicacao.objects.filter(pk=publicacao_id).first()
            autor = Utilizador.objects.filter(pk=utilizador_id).first()
            if publicacao and autor and texto:
                Comentario.objects.create(
                    publicacao=publicacao,
                    autor=autor,
                    texto=texto,
                )
        elif acao == 'like':
            publicacao = Publicacao.objects.filter(pk=publicacao_id).first()
            utilizador = Utilizador.objects.filter(pk=utilizador_id).first()
            if publicacao and utilizador:
                _, created = Like.objects.get_or_create(publicacao=publicacao, utilizador=utilizador)
                if created:
                    publicacao.likes += 1
                    publicacao.save(update_fields=['likes'])
        elif acao == 'publicar_imagem':
            image_url = (request.POST.get('image_url') or '').strip()
            caption = (request.POST.get('caption') or '').strip()
            autor = Utilizador.objects.filter(pk=utilizador_id).first()
            if autor and (image_url.startswith('http://') or image_url.startswith('https://')):
                conteudo = f'Imagem: {image_url}'
                if caption:
                    conteudo = f'{conteudo}\nLegenda: {caption}'
                Publicacao.objects.create(
                    autor=autor,
                    conteudo=conteudo,
                )
        elif acao == 'remover_publicacao':
            publicacao = Publicacao.objects.filter(pk=publicacao_id).first()
            utilizador = Utilizador.objects.filter(pk=utilizador_id).first()
            if publicacao and utilizador and publicacao.autor_id == utilizador.id:
                publicacao.delete()
        elif acao == 'remover_like':
            publicacao = Publicacao.objects.filter(pk=publicacao_id).first()
            utilizador = Utilizador.objects.filter(pk=utilizador_id).first()
            if publicacao and utilizador:
                deleted_count, _ = Like.objects.filter(publicacao=publicacao, utilizador=utilizador).delete()
                if deleted_count > 0 and publicacao.likes > 0:
                    publicacao.likes -= 1
                    publicacao.save(update_fields=['likes'])
        elif acao == 'remover_comentario':
            comentario_id = request.POST.get('comentario_id')
            comentario = Comentario.objects.filter(pk=comentario_id).first()
            utilizador = Utilizador.objects.filter(pk=utilizador_id).first()
            if comentario and utilizador and comentario.autor_id == utilizador.id:
                comentario.delete()

        return redirect('publicacoes')

    lista_publicacoes = Publicacao.objects.select_related('autor').prefetch_related('comentarios__autor', 'likes_rel').order_by('-criado_em')
    utilizadores = Utilizador.objects.order_by('nome')
    publicacoes = []
    for p in lista_publicacoes:
        image_url = None
        caption = None
        text = p.conteudo
        if text.startswith('Imagem:'):
            candidate = text.replace('Imagem:', '', 1).strip()
            if '\nLegenda:' in candidate:
                parts = candidate.split('\nLegenda:', 1)
                candidate = parts[0].strip()
                caption = parts[1].strip() or None
            if candidate.startswith('http://') or candidate.startswith('https://'):
                image_url = candidate
        publicacoes.append({'obj': p, 'image_url': image_url, 'caption': caption})
    return render(request, 'main/publicacoes.html', {'publicacoes': publicacoes, 'utilizadores': utilizadores})


def utilizadores(request):
    erro_login = None
    erro_registo = None

    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'login':
            username = (request.POST.get('username') or '').strip()
            password = request.POST.get('password') or ''
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('utilizadores')
            erro_login = 'Credenciais invalidas.'

        elif acao == 'registar':
            username = (request.POST.get('username') or '').strip()
            nome = (request.POST.get('nome') or '').strip()
            email = (request.POST.get('email') or '').strip()
            password = request.POST.get('password') or ''

            if not username or not nome or not email or not password:
                erro_registo = 'Preenche os campos obrigatorios do registo.'
            elif User.objects.filter(username=username).exists():
                erro_registo = 'Esse username ja existe.'
            elif Utilizador.objects.filter(email=email).exists():
                erro_registo = 'Esse email ja esta registado.'
            else:
                User.objects.create_user(username=username, email=email, password=password)
                Utilizador.objects.create(nome=nome, email=email)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('utilizadores')

        elif acao == 'logout':
            logout(request)
            return redirect('utilizadores')

    lista_utilizadores = Utilizador.objects.prefetch_related('publicacoes').order_by('nome')
    return render(
        request,
        'main/utilizadores.html',
        {
            'utilizadores': lista_utilizadores,
            'erro_login': erro_login,
            'erro_registo': erro_registo,
        },
    )
