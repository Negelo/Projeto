from django.db import models


class Utilizador(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Publicacao(models.Model):
    autor = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='publicacoes')
    conteudo = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Publicacao de {self.autor.nome} ({self.pk})'


class Comentario(models.Model):
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario {self.pk} em publicacao {self.publicacao_id}'


class Like(models.Model):
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE, related_name='likes_rel')
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='likes')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['publicacao', 'utilizador'], name='unique_like_por_utilizador_publicacao')
        ]

    def __str__(self):
        return f'Like de {self.utilizador.nome} na publicacao {self.publicacao_id}'
