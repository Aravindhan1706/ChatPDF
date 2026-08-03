from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Request model for asking questions."""

    question: str


class ChatResponse(BaseModel):
    """Response model for chat."""

    answer: str
