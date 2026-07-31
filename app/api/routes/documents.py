from fastapi import APIRouter, Depends, File, UploadFile

from app.core.dependencies import (
    get_document_processor,
    get_document_service,
    get_vector_store_service,
)
from app.services.document_processor import DocumentProcessor
from app.services.document_service import DocumentService
from app.services.vector_store_service import VectorStoreService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    document_service: DocumentService = Depends(get_document_service),
    document_processor: DocumentProcessor = Depends(get_document_processor),
    vector_store: VectorStoreService = Depends(get_vector_store_service),
) -> dict:
    """Upload a PDF."""

    result = document_service.save_document(file)

    text = document_processor.extract_text(result["path"])

    chunks = document_processor.chunk_text(text)

    vector_store.add_documents(
        chunks=chunks,
        filename=result["filename"],
    )

    return {
        "message": "Document processed successfully.",
        "chunks": len(chunks),
    }
