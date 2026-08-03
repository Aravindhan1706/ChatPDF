from app.services.chat_service import ChatService
from app.services.document_processor import DocumentProcessor
from app.services.document_service import DocumentService
from app.services.llm_service import LLMService
from app.services.vector_store_service import VectorStoreService

document_service = DocumentService()
document_processor = DocumentProcessor()
vector_store_service = VectorStoreService()
llm_service = LLMService()
chat_service = ChatService(
    vector_store=vector_store_service,
    llm_service=llm_service,
)


def get_document_service() -> DocumentService:
    """Return the document service."""
    return document_service


def get_document_processor() -> DocumentProcessor:
    """Return the document processor."""
    return document_processor


def get_vector_store_service() -> VectorStoreService:
    """Return the vector store service."""
    return vector_store_service


def get_chat_service() -> ChatService:
    """Return the chat service."""
    return chat_service
