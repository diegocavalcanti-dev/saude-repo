# Usando a imagem oficial do Python
FROM python:3.13-slim as python-base

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências primeiro para otimizar o cache
COPY pyproject.toml poetry.lock /app/

# Instalar o Poetry e as dependências sem o modo de desenvolvimento
RUN pip install --no-cache-dir poetry && poetry install --no-dev

# Copiar o restante do código da aplicação
COPY . /app/

# Expor a porta do Django
EXPOSE 8000

# Rodar o servidor Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]