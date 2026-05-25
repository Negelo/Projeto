from django.contrib import admin

from .models import Comentario, Like, Publicacao, Utilizador


@admin.register(Utilizador)
class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'likes', 'criado_em')
    list_filter = ('criado_em',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'publicacao', 'autor', 'criado_em')
    list_filter = ('criado_em',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'publicacao', 'utilizador', 'criado_em')
    list_filter = ('criado_em',)
