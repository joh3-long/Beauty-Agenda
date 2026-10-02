from django.db import models


class Produto(models.Model):

    CATEGORIAS = [
        ("skincare", "Skincare"),
        ("maquiagem", "Maquiagem"),
        ("cabelos", "Cabelos"),
        ("perfume", "Perfume"),
        ("unhas", "Unhas"),
    ]

    nome = models.CharField(
        max_length=150
    )

    marca = models.CharField(
        max_length=100
    )

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    descricao = models.TextField(
        blank=True
    )

    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    avaliacao = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome