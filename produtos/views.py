from django.shortcuts import redirect, render

from .forms import ProdutoForm
from .models import Produto


def inicio(request):
    produtos = Produto.objects.all()

    return render(
        request,
        "produtos/inicio.html",
        {"produtos": produtos}
    )


def cadastrar_produto(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("inicio")

    else:
        form = ProdutoForm()

    return render(
        request,
        "produtos/cadastrar.html",
        {"form": form}
    )