from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto

        fields = [
            "nome",
            "marca",
            "categoria",
            "descricao",
            "preco",
            "avaliacao",
        ]

        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "placeholder": "Nome do produto"
                }
            ),

            "marca": forms.TextInput(
                attrs={
                    "placeholder": "Marca"
                }
            ),

            "descricao": forms.Textarea(
                attrs={
                    "placeholder": "Descrição do produto",
                    "rows": 4
                }
            ),

            "preco": forms.NumberInput(
                attrs={
                    "placeholder": "0.00",
                    "step": "0.01"
                }
            ),

            "avaliacao": forms.NumberInput(
                attrs={
                    "placeholder": "1 a 5",
                    "min": "1",
                    "max": "5"
                }
            ),
        }