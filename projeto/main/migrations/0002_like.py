from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_rel', to='main.publicacao')),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='main.utilizador')),
            ],
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('publicacao', 'utilizador'), name='unique_like_por_utilizador_publicacao'),
        ),
    ]
