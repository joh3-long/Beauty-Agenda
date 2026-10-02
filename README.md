Beauty Agenda

Sistema web desenvolvido em Django para organizar produtos de beleza em um catálogo pessoal.

O usuário pode cadastrar produtos de beleza, informando nome, marca, categoria, descrição, preço e avaliação.

Tecnologias Utilizadas
Python
Django
SQLite
HTML
CSS próprio
Pré-requisitos
Python 3.10 ou superior
Git
Git Bash
Visual Studio Code
Como Instalar e Rodar

Clone o projeto:

git clone URL_DO_REPOSITORIO
cd agenda-beleza-django
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Depois, acesse no navegador:

http://127.0.0.1:8000/

Funcionalidades do Sistema
Cadastro de produtos de beleza
Listagem dos produtos cadastrados
Adicionar novos produtos
Informar nome do produto
Informar marca
Selecionar categoria
Adicionar descrição
Informar preço
Adicionar avaliação
Visualizar os produtos cadastrados
Banco de dados SQLite
Interface simples
CSS separado dos arquivos Python
Categorias de Produtos

O sistema possui categorias relacionadas ao tema de beleza:

Skincare
Maquiagem
Cabelos
Perfume
Unhas
Informações dos Produtos

Cada produto cadastrado possui:

Nome
Marca
Categoria
Descrição
Preço
Avaliação
Data de cadastro
Estrutura do Projeto
agenda-beleza-django/
│
├── beleza/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── produtos/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   └── produtos/
│       ├── lista.html
│       └── formulario.html
│
├── static/
│   └── css/
│       └── estilo.css
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
Banco de Dados

O projeto utiliza o SQLite como banco de dados para armazenar os produtos cadastrados.

Interface

O sistema possui uma interface simples relacionada ao tema de beleza, utilizando tons de rosa e uma organização simples para facilitar o cadastro e a visualização dos produtos.

O CSS foi desenvolvido separadamente dos arquivos Python e Django.

Como Cadastrar um Produto
Acesse o sistema pelo navegador.
Clique em "+ Cadastrar produto".
Informe o nome do produto.
Informe a marca.
Selecione uma categoria.
Adicione uma descrição.
Informe o preço.
Informe a avaliação.
Clique em "Cadastrar produto".

Após o cadastro, o produto será exibido na página principal do sistema.

Objetivo do Projeto

O objetivo do projeto é desenvolver um sistema web simples utilizando Python e Django para organizar produtos de beleza em um catálogo.

O projeto permite praticar conceitos básicos de desenvolvimento web, como:

Python
Django
Models
Forms
Views
URLs
Templates
HTML
CSS
SQLite
Ambiente virtual
Git
Git Bash
Execução do Projeto

Para executar o projeto novamente:

source venv/Scripts/activate
python manage.py runserver

O sistema ficará disponível em:

http://127.0.0.1:8000/

Autor

Jordanna de Jesus Ribeiro Porto
