from pydantic import BaseModel


class UploadResponse(BaseModel):
    """Response returned after a successful PDF upload."""

    message: str
    chunks: int
