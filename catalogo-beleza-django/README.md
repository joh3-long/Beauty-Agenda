# Agenda de Beleza

Sistema web simples para cadastro e organização de serviços de beleza, desenvolvido com Python e Django.

## 2. Tecnologias Utilizadas

- Python
- Django
- SQLite
- HTML
- CSS

## 3. Pré-requisitos

- Python 3.10 ou superior
- Git e Git Bash

## 4. Como Instalar e Rodar

No Git Bash:

```bash
git clone URL_DO_SEU_REPOSITORIO
cd agenda-beleza-django
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## 5. Funcionalidades do Sistema

- Cadastro de usuário.
- Login e logout.
- Página principal protegida por login.
- Cadastro de serviços de beleza.
- Listagem dos serviços cadastrados pelo usuário.
- Edição de serviços.
- Exclusão de serviços com confirmação.
- Campos de nome do serviço, descrição, categoria, preço, status e data automática de cadastro.
- CSS separado do HTML.

## 6. Autor

Jordanna de Jesus Ribeiro Porto  
Turma: 982100
