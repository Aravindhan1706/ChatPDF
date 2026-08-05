from pathlib import Path
from shutil import copyfileobj

from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader

from app.core.exceptions import DocumentProcessingError
from app.schemas.document_metadata import DocumentMetadata


class DocumentService:
    """Service for handling document operations."""

    STORAGE_PATH = Path("storage/documents")

    def save_document(self, file: UploadFile) -> DocumentMetadata:
        """Validate and save an uploaded PDF."""

        try:
            if file.content_type != "application/pdf":
                raise DocumentProcessingError("Only PDF files are allowed.")

            self.STORAGE_PATH.mkdir(
                parents=True,
                exist_ok=True,
            )

            destination = self.STORAGE_PATH / file.filename

            with destination.open("wb") as buffer:
                copyfileobj(file.file, buffer)

            file.file.seek(0)

            return DocumentMetadata(
                filename=file.filename,
                content_type=file.content_type,
                size=destination.stat().st_size,
                path=destination.as_posix(),
            )

        except DocumentProcessingError:
            raise

        except Exception as exc:
            raise DocumentProcessingError(
                "Failed to save the uploaded document."
            ) from exc

    def extract_text(self, pdf_path: str) -> str:
        """Extract all text from a PDF."""

        try:
            loader = PyPDFLoader(pdf_path)

            documents = loader.load()

            text = "\n".join(document.page_content for document in documents)

            return text

        except Exception as exc:
            raise DocumentProcessingError(
                "Failed to extract text from the uploaded document."
            ) from exc
