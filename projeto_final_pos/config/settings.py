from pydantic import BaseModel
from typing import List
import yaml
import os

class LLMConfig(BaseModel):
    model: str
    temperature: float
    top_k: int
    top_p: float
    repeat_penalty: float

class EmbeddingsConfig(BaseModel):
    model_name: str

class CSVConfig(BaseModel):
    separator: str
    max_file_size_mb: int
    encodings: List[str]

class RetrieverConfig(BaseModel):
    top_k: int

class AppConfig(BaseModel):
    llm: LLMConfig
    embeddings: EmbeddingsConfig
    csv: CSVConfig
    retriever: RetrieverConfig

def load_config(path: str = None) -> AppConfig:
    path = path or os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(path, "r", encoding="utf-8") as f:
        config_dict = yaml.safe_load(f)
    return AppConfig(**config_dict)
