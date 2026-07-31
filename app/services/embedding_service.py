from langchain_ollama import OllamaEmbeddings


class EmbeddingService:
    """Service responsible for generating embeddings."""

    def __init__(self) -> None:
        self.embedding_model = OllamaEmbeddings(
            model="mxbai-embed-large",
        )

    def get_embedding(self, text: str) -> list[float]:
        """Generate an embedding for a single text."""

        return self.embedding_model.embed_query(text)

    def get_embeddings(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for multiple texts."""

        return self.embedding_model.embed_documents(texts)
