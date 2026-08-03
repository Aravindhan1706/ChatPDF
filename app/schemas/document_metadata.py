from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    """Metadata for an uploaded document."""

    document_id: UUID = Field(default_factory=uuid4)
    filename: str
    path: str
    size: int
    content_type: str
