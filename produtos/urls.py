from django.urls import path

from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path(
        "cadastrar/",
        views.cadastrar_produto,
        name="cadastrar_produto"
    ),
]