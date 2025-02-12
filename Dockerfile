# Usando a imagem oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências para o contêiner
COPY pyproject.toml poetry.lock /app/

# Instalar dependências
RUN pip install poetry && poetry install --no-dev

# Copiar o código da aplicação
COPY . /app/

# Expor a porta do Django
EXPOSE 8000

# Rodar o servidor Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]