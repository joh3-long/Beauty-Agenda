from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_servicos, name="lista_servicos"),
    path("cadastro/", views.cadastrar, name="cadastro"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("servico/adicionar/", views.adicionar_servico, name="adicionar_servico"),
    path("servico/<int:pk>/editar/", views.editar_servico, name="editar_servico"),
    path("servico/<int:pk>/excluir/", views.excluir_servico, name="excluir_servico"),
]
