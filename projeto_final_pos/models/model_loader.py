from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from config.settings import AppConfig

def load_embeddings(config: AppConfig):
    return HuggingFaceEmbeddings(model_name=config.embeddings.model_name)

def load_llm(config: AppConfig):
    return Ollama(
        model=config.llm.model,
        temperature=config.llm.temperature,
        top_k=config.llm.top_k,
        top_p=config.llm.top_p,
        repeat_penalty=config.llm.repeat_penalty,
    )
