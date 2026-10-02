from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CadastroForm, ServicoForm
from .models import Servico

def cadastrar(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("lista_servicos")
    else:
        form = CadastroForm()
    return render(request, "servicos/cadastrar.html", {"form": form})

@login_required
def lista_servicos(request):
    servicos = Servico.objects.filter(usuario=request.user)
    return render(request, "servicos/lista.html", {"servicos": servicos})

@login_required
def adicionar_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.usuario = request.user
            servico.save()
            messages.success(request, "Serviço adicionado com sucesso!")
            return redirect("lista_servicos")
    else:
        form = ServicoForm()
    return render(request, "servicos/form.html", {"form": form, "titulo": "Adicionar serviço"})

@login_required
def editar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, "Serviço atualizado com sucesso!")
            return redirect("lista_servicos")
    else:
        form = ServicoForm(instance=servico)
    return render(request, "servicos/form.html", {"form": form, "titulo": "Editar serviço"})

@login_required
def excluir_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk, usuario=request.user)
    if request.method == "POST":
        servico.delete()
        messages.success(request, "Serviço excluído com sucesso!")
        return redirect("lista_servicos")
    return render(request, "servicos/excluir.html", {"servico": servico})
