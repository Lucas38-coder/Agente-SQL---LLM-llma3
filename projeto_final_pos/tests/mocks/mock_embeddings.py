class MockEmbeddings:
    def embed_documents(self, texts):
        # Retorna vetores fixos falsos (quantidade igual ao número de textos)
        return [[0.1] * 384 for _ in texts]
