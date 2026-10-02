from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name="Servico",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=150)),
                ("descricao", models.TextField(blank=True)),
                ("categoria", models.CharField(choices=[("cabelo", "Cabelo"), ("unhas", "Unhas"), ("pele", "Pele"), ("maquiagem", "Maquiagem")], max_length=20)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=8)),
                ("status", models.CharField(choices=[("disponivel", "Disponível"), ("realizado", "Já realizado")], default="disponivel", max_length=20)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("usuario", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-criado_em"]},
        ),
    ]
