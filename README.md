# Beauty Agenda

Sistema web desenvolvido em **Python e Django** para organizar produtos de beleza em um catálogo pessoal.

O usuário pode cadastrar produtos de beleza, informando **nome, marca, categoria, descrição, preço e avaliação**.

## Tecnologias Utilizadas

* Python
* Django
* SQLite
* HTML
* CSS

## Pré-requisitos

Para executar o projeto, é necessário ter instalado:

* Python 3.10 ou superior
* Git
* Git Bash
* Visual Studio Code

## Como Instalar e Rodar

### 1. Clone o projeto

No Git Bash, execute:

```bash
git clone URL_DO_REPOSITORIO
```

Depois, entre na pasta do projeto:

```bash
cd agenda-beleza-django
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

No Git Bash:

```bash
source venv/Scripts/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Depois, acesse o sistema pelo navegador:

**http://127.0.0.1:8000/**

## Funcionalidades do Sistema

O sistema possui as seguintes funcionalidades:

* Cadastro de produtos de beleza;
* Listagem dos produtos cadastrados;
* Adição de novos produtos;
* Cadastro do nome do produto;
* Cadastro da marca;
* Seleção de categoria;
* Adição de descrição;
* Cadastro do preço;
* Cadastro de avaliação;
* Visualização dos produtos cadastrados;
* Armazenamento dos dados utilizando SQLite;
* Interface simples e organizada;
* CSS separado dos arquivos Python.

## Categorias de Produtos

O sistema possui categorias relacionadas ao tema de beleza:

* Skincare
* Maquiagem
* Cabelos
* Perfume
* Unhas

## Informações dos Produtos

Cada produto cadastrado possui:

* Nome;
* Marca;
* Categoria;
* Descrição;
* Preço;
* Avaliação;
* Data de cadastro.

## Estrutura do Projeto

```text
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
```

## Banco de Dados

O projeto utiliza o **SQLite** como banco de dados para armazenar as informações dos produtos cadastrados.

O SQLite é utilizado por ser simples e adequado para projetos pequenos e acadêmicos.

## Interface

O sistema possui uma interface simples relacionada ao tema de beleza, utilizando **tons de rosa** e uma organização que facilita o cadastro e a visualização dos produtos.

O CSS foi desenvolvido separadamente dos arquivos Python e Django, ficando localizado na pasta:

```text
static/css/estilo.css
```

## Como Cadastrar um Produto

Para cadastrar um novo produto:

1. Acesse o sistema pelo navegador.
2. Clique em **"+ Cadastrar produto"**.
3. Informe o nome do produto.
4. Informe a marca.
5. Selecione uma categoria.
6. Adicione uma descrição.
7. Informe o preço.
8. Informe a avaliação.
9. Clique em **"Cadastrar produto"**.

Após o cadastro, o produto será exibido na página principal do sistema.

## Objetivo do Projeto

O objetivo do projeto é desenvolver um sistema web simples utilizando **Python e Django** para organizar produtos de beleza em um catálogo pessoal.

O projeto permite praticar conceitos básicos de desenvolvimento web, como:

* Python;
* Django;
* Models;
* Forms;
* Views;
* URLs;
* Templates;
* HTML;
* CSS;
* SQLite;
* Ambiente virtual;
* Git;
* Git Bash.

## Execução do Projeto

Para executar o projeto novamente, abra o Git Bash na pasta do projeto e ative o ambiente virtual:

```bash
source venv/Scripts/activate
```

Depois, execute:

```bash
python manage.py runserver
```

O sistema ficará disponível no endereço:

**http://127.0.0.1:8000/**

## Autor

**Jordanna de Jesus Ribeiro Porto**
