from fastapi import APIRouter, File, UploadFile

from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)) -> dict:
    """Upload a PDF."""

    document_service = DocumentService()

    result = document_service.save_document(file)

    extracted_text = document_service.extract_text(result["path"])

    return {
        **result,
        "text": extracted_text,
    }
