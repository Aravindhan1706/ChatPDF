from fastapi import APIRouter, Depends, File, UploadFile

from app.core.dependencies import (
    get_document_processor,
    get_document_service,
    get_vector_store_service,
)
from app.schemas.document import UploadResponse
from app.services.document_processor import DocumentProcessor
from app.services.document_service import DocumentService
from app.services.vector_store_service import VectorStoreService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload", response_model=UploadResponse)
async def upload_document(
    file: UploadFile = File(...),
    document_service: DocumentService = Depends(get_document_service),
    document_processor: DocumentProcessor = Depends(get_document_processor),
    vector_store: VectorStoreService = Depends(get_vector_store_service),
) -> UploadResponse:
    """Upload a PDF."""

    document = document_service.save_document(file)

    text = document_processor.extract_text(document.path)

    chunks = document_processor.chunk_text(text)

    vector_store.add_documents(
        chunks=chunks,
        document=document,
    )

    return UploadResponse(
        message="Document processed successfully.",
        chunks=len(chunks),
    )
