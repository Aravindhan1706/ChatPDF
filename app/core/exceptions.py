from http import HTTPStatus


class ChatPDFException(Exception):
    """Base exception for the ChatPDF application."""

    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code: str = "CHATPDF_ERROR"

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class DocumentProcessingError(ChatPDFException):
    """Raised when document processing fails."""

    status_code = HTTPStatus.BAD_REQUEST
    error_code = "DOCUMENT_PROCESSING_ERROR"


class VectorStoreError(ChatPDFException):
    """Raised when vector database operations fail."""

    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code = "VECTOR_STORE_ERROR"


class LLMError(ChatPDFException):
    """Raised when the language model fails."""

    status_code = HTTPStatus.SERVICE_UNAVAILABLE
    error_code = "LLM_ERROR"
