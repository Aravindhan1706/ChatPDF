class ChatPDFException(Exception):
    """Base exception for the ChatPDF application."""

    def __init__(
        self,
        message: str,
    ) -> None:
        self.message = message
        super().__init__(message)


class DocumentProcessingError(ChatPDFException):
    """Raised when a document cannot be processed."""


class VectorStoreError(ChatPDFException):
    """Raised when vector store operations fail."""


class LLMError(ChatPDFException):
    """Raised when the language model fails."""
