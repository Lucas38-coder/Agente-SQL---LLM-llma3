import pandas as pd
from typing import Optional
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from typing import Any
from config.settings import AppConfig
import logging


logger = logging.getLogger(__name__)

class CSVLoader:
    def __init__(self, config: AppConfig, embeddings: Any):
        self.config = config
        self.embeddings = embeddings
        self.vectorstore: Optional[FAISS] = None
        self.text_data: Optional[str] = None

    def load_csv(self, file_path: str) -> str:
        df = self._try_read_csv(file_path)
        if df is None or df.empty:
            return "❌ O CSV está vazio ou inválido."

        df.dropna(axis=1, how='all', inplace=True)
        df.fillna("", inplace=True)
        self.text_data = df.to_string(index=False)

        texts = [
            row.to_string()
            for _, row in df.iterrows()
            if isinstance(row.to_string(), str) and row.to_string().strip()
        ]

        if not texts:
            return "❌ Nenhum dado válido encontrado para vetorização."

        logger.info("Iniciando vetorização dos documentos com FAISS...")
        docs = [Document(page_content=txt) for txt in texts]
        self.vectorstore = FAISS.from_documents(docs, self.embeddings)

        return "✅ Arquivo CSV carregado e vetorizado com sucesso!"

    def _try_read_csv(self, file_path: str) -> Optional[pd.DataFrame]:
        sep = self.config.csv.separator
        for enc in self.config.csv.encodings:
            try:
                df = pd.read_csv(file_path, sep=sep, encoding=enc)
                logger.info(f"Arquivo CSV lido com sucesso usando encoding: {enc}")
                return df
            except UnicodeDecodeError:
                logger.warning(f"Falha ao ler com encoding: {enc}")
        logger.error("Não foi possível ler o arquivo CSV com os encodings disponíveis.")
        return None
