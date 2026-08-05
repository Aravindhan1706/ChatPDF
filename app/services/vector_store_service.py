from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

from app.core.config import settings
from app.core.exceptions import VectorStoreError
from app.schemas.document_metadata import DocumentMetadata


class VectorStoreService:
    """Service responsible for storing and retrieving document vectors."""

    def __init__(self) -> None:
        self.embedding_model = OllamaEmbeddings(
            model=settings.models.embedding_model,
        )

        self.vector_store = Chroma(
            collection_name="documents",
            embedding_function=self.embedding_model,
            persist_directory="./chroma_db",
        )

    def add_documents(
        self,
        chunks: list[str],
        document: DocumentMetadata,
    ) -> None:
        """Store document chunks in ChromaDB."""

        try:
            documents = []

            for index, chunk in enumerate(chunks):
                documents.append(
                    Document(
                        page_content=chunk,
                        metadata={
                            "document_id": str(document.document_id),
                            "filename": document.filename,
                            "chunk": index,
                        },
                    )
                )

            self.vector_store.add_documents(documents)

        except Exception as exc:
            raise VectorStoreError("Failed to store document embeddings.") from exc

    def similarity_search(
        self,
        query: str,
        k: int = 5,
    ) -> list[Document]:
        """Search similar document chunks."""

        try:
            return self.vector_store.similarity_search(
                query=query,
                k=k,
            )

        except Exception as exc:
            raise VectorStoreError("Failed to search the vector database.") from exc
