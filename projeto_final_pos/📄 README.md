📄 README.md

# CSV QA System - RumoLog

Este projeto permite fazer perguntas interativas a partir de arquivos CSV utilizando técnicas de vetorização e LLM (Large Language Models).  
A interface é construída com Gradio e tem a identidade visual da RumoLog.

---

## Como usar

1. Clone o projeto:

```bash
git clone https://github.com/seu_usuario/csv_qa.git
cd csv_qa
Instale as dependências:

pip install -r requirements.txt
Configure as variáveis de ambiente (opcional):

Execute o sistema:

python main.py
Acesse a interface web no navegador.

Estrutura
core/ - Lógica principal de carregamento e QA

models/ - Carregamento dos modelos LLM e embeddings

interface/ - Interface Gradio personalizada

config/ - Arquivo de configuração YAML e carregamento

tests/ - Testes automatizados

cli/ - (Opcional) CLI para uso via terminal

Testes
Para rodar testes use:
pytest tests/


Contribuições são bem-vindas!
Abra issues para dúvidas ou sugestões.

Contato
Desenvolvido para RumoLog 🚛
Lucas - Criador de Conteúdo & Mentor em Dados



