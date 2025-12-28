# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho no container
WORKDIR /app

# Copia o requirements.txt (ou seus arquivos de dependências)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código para o container
COPY . .

# Expõe a porta padrão do uvicorn
EXPOSE 8000

# Comando para iniciar o servidor FastAPI com reload desabilitado em produção
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
