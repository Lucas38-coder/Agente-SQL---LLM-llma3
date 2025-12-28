import logging
from config.settings import load_config
from models.model_loader import load_embeddings, load_llm
from core.csv_loader import CSVLoader
from core.qa_engine import QAEngine
from interface.gradio_app import build_interface

# Configura o logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def main():
    # 1. Carrega configurações
    config = load_config()

    # 2. Instancia modelos
    embeddings = load_embeddings(config)
    llm = load_llm(config)

    # 3. Inicializa carregador e engine de perguntas
    loader = CSVLoader(config, embeddings)
    qa_engine = QAEngine(config, llm, vectorstore_getter=lambda: loader.vectorstore)

    # 4. Constrói e lança interface
    interface = build_interface(loader, qa_engine)
    interface.launch()

if __name__ == "__main__":
    main()
