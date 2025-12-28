from core.qa_engine import QAEngine
from config.settings import load_config
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS

class MockLLM:
    def invoke(self, prompt: str):
        return "Essa é uma resposta de teste."

class MockRetriever:
    def get_relevant_documents(self, query: str):
        return [Document(page_content="Lucas tem 30 anos."), Document(page_content="Maria tem 25 anos.")]

class MockVectorstore:
    def as_retriever(self, **kwargs):
        return MockRetriever()

def test_qa_response():
    config = load_config()
    vectorstore = MockVectorstore()
    qa_engine = QAEngine(config, llm=MockLLM(), vectorstore_getter=lambda: vectorstore)

    resposta = qa_engine.ask("Quem é mais velha?")
    assert "teste" in resposta.lower()
