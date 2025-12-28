import os
import pandas as pd
from core.csv_loader import CSVLoader
from config.settings import load_config
from tests.mocks.mock_embeddings import MockEmbeddings

def test_load_valid_csv(tmp_path):
    # Cria CSV temporário
    csv_path = tmp_path / "test.csv"
    df = pd.DataFrame({
        "Nome": ["Lucas", "Maria"],
        "Idade": [30, 25]
    })
    df.to_csv(csv_path, sep=";", index=False)

    config = load_config()
    loader = CSVLoader(config, embeddings=MockEmbeddings())

    result = loader.load_csv(str(csv_path))
    assert "✅" in result
    assert loader.vectorstore is not None
    assert loader.text_data is not None
