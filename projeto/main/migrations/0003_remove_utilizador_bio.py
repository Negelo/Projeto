from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilizador',
            name='bio',
        ),
    ]
