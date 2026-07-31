from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings


class VectorStoreService:
    """Service responsible for storing and retrieving document vectors."""

    def __init__(self) -> None:
        self.embedding_model = OllamaEmbeddings(
            model="mxbai-embed-large",
        )

        self.vector_store = Chroma(
            collection_name="documents",
            embedding_function=self.embedding_model,
            persist_directory="./chroma_db",
        )

    def add_documents(
        self,
        chunks: list[str],
        filename: str,
    ) -> None:
        """Store document chunks in ChromaDB."""

        documents = []

        for index, chunk in enumerate(chunks):
            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "filename": filename,
                        "chunk": index,
                    },
                )
            )

        self.vector_store.add_documents(documents)
