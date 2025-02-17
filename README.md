# 🚀 API de Gerenciamento de Consultas Médicas

Este projeto é uma API Restful desenvolvida em **Django** e **Django REST Framework**, com **PostgreSQL** como banco de dados e **Docker** para facilitar a configuração do ambiente. O objetivo é permitir o gerenciamento de consultas médicas e profissionais de saúde.

## 📄 **Requisitos do Projeto**

- **Linguagem:** Python  
- **Framework:** Django e Django REST Framework  
- **Gerenciador de dependências:** Poetry  
- **Banco de dados:** PostgreSQL  
- **Padrão:** Rest API  
- **Containerização:** Docker  
- **Testes:** APITestCase do Django REST Framework  

## 🏢 **Configuração do Ambiente**

### 1. **Clone o repositório**
```bash
git clone https://github.com/diegocavalcanti-dev/saude-repo
cd saude-repo
```
### 2. Instale o Poetry (caso não tenha instalado)
```bash
pip install poetry
```
### 3. Instale as dependências
```bash
poetry install
```
### 4. Configuração do banco de dados
Altere o arquivo settings.py para conectar ao PostgreSQL:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Crie o banco no PostgreSQL:
```bash
CREATE DATABASE seu_banco;
GRANT ALL PRIVILEGES ON DATABASE seu_banco TO seu_usuario;
```
### 5. Execute as migrações
```bash
poetry python manage.py migrate
```
### 6. Crie um superusuário
```bash
poetry python manage.py createsuperuser
````
### 7. Inicie o servidor
```bash
poetry python manage.py runserver
```
A API estará disponível em: http://127.0.0.1:8000/api/

## 🌐 Executando com Docker

### 1. Construa a imagem e suba os containers
```bash
docker compose up -d --build
```
### 2. Acesse o container para rodar migrações
```bash
docker exec -it api_container python manage.py migrate
```

## 🎲 Endpoints da API

## 👩‍🏥 Profissionais de Saúde
- **Criar:** POST /api/profissionais/
- **Listar:** GET /api/profissionais/
- Buscar por ID: GET /api/profissionais/{id}/
- Atualizar: PATCH /api/profissionais/{id}/
- Deletar: DELETE /api/profissionais/{id}/

## 👨‍⚕️ Consultas
- Criar: POST /api/consultas/
- Listar: GET /api/consultas/
- Buscar por ID: GET /api/consultas/{id}/
- Atualizar: PATCH /api/consultas/{id}/
- Deletar: DELETE /api/consultas/{id}/
- Buscar por profissional: GET /api/consultas/?profissional_id={id}

## 🎮 Executando os Testes

Rodar os testes unitários com:
```bash
poetry python manage.py test
```

## 📝 Tecnologias Utilizadas
- Django & Django REST Framework
- PostgreSQL
- Poetry para gestão de dependências
- Docker para ambiente isolado
- Testes com APITestCase

## 📢 Contato

Caso tenha dúvidas, entre em contato pelo e-mail cavalcantidiego@hotmail.com

