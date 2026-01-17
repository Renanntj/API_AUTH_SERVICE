# API Auth Service

Projeto educacional de **API de autenticação** desenvolvido com foco em aprendizado prático de backend em Python utilizando **FastAPI**.  
Este repositório demonstra conceitos fundamentais de autenticação, segurança de senhas e organização de código em APIs REST.

## Visão Geral

Esta API tem como objetivo fornecer um fluxo básico de autenticação de usuários, incluindo:

- Registro de usuários
- Hash de senhas com bcrypt
- Autenticação via OAuth2
- Estrutura modular de rotas
- Base para expansão com JWT e controle de permissões

O projeto foi construído com foco em **boas práticas**, clareza de código e evolução progressiva — ideal para desenvolvedores backend em fase de aprendizado.

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Passlib (bcrypt)
- OAuth2PasswordBearer
- Uvicorn

## Estrutura do Projeto

```text
api_auth_project/
├── main.py
├── auth_routes.py
├── models/
├── schemas/
├── database/
└── requirements.txt
```

## Conceitos Aplicados

- Arquitetura de API REST
- Separação de responsabilidades
- Segurança no armazenamento de senhas
- Padrões de autenticação
- Organização de rotas e dependências
- Validação de dados com schemas

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
uvicorn main:app --reload
```

5. Acesse a documentação automática:
- Swagger: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc


## Autor

Projeto desenvolvido para fins educacionais por um desenvolvedor backend em formação.

By Renan Alves