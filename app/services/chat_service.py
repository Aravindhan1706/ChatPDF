from langchain_core.documents import Document

from app.services.llm_service import LLMService
from app.services.vector_store_service import VectorStoreService


class ChatService:
    """Service responsible for answering questions."""

    def __init__(
        self,
        vector_store: VectorStoreService,
        llm_service: LLMService,
    ) -> None:
        self.vector_store = vector_store
        self.llm_service = llm_service

    def retrieve_context(
        self,
        question: str,
    ) -> list[Document]:
        """Retrieve relevant document chunks."""

        return self.vector_store.similarity_search(question)

    def ask(
        self,
        question: str,
    ) -> str:
        """Answer a question using RAG."""

        documents = self.retrieve_context(question)

        context = "\n\n".join(document.page_content for document in documents)

        return self.llm_service.generate_answer(
            question=question,
            context=context,
        )
