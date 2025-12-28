from langchain.llms.base import LLM
from langchain_community.vectorstores import FAISS
from config.settings import AppConfig
import logging

logger = logging.getLogger(__name__)

class QAEngine:
    def __init__(self, config: AppConfig, llm: LLM, vectorstore_getter: callable):
        self.config = config
        self.llm = llm
        self.vectorstore_getter = vectorstore_getter  # função que retorna o FAISS atual

    def ask(self, question: str) -> str:
        if not question.strip():
            return "❌ Por favor, digite uma pergunta válida."

        vectorstore: FAISS = self.vectorstore_getter()
        if not vectorstore:
            return "❌ Nenhum CSV carregado ainda."

        retriever = vectorstore.as_retriever(
            search_kwargs={"k": self.config.retriever.top_k}
        )
        context_docs = retriever.get_relevant_documents(question)

        if not context_docs:
            return "❌ Nenhum contexto relevante foi encontrado para essa pergunta."

        context = "\n\n".join([doc.page_content for doc in context_docs])

        prompt = f"""Você é um especialista em análise de dados e banco de dados. Você irá receber um arquivo CSV com os metadados da empresa e precisa fornecer uma resposta com base na pergunta do usuário sobre a base, como por exemplo: Onde estão as informações que ele está buscando? qual tabela? qual esquema? quais as colunas dessa tabela? um exemplo de query, a tabela está em uso sim ou não? As colunas categoria e subcategoria descrevem onde encontrar essas informações. Responda as perguntas em português. 

### DADOS:
{context}

### PERGUNTA:
{question}

### RESPOSTA:"""

        logger.info("Enviando prompt para o modelo...")
        try:
            resposta = self.llm.invoke(prompt)
            return resposta.strip()
        except Exception as e:
            logger.error(f"Erro ao invocar o modelo: {e}")
            return f"❌ Erro ao processar a pergunta: {str(e)}"
