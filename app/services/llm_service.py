from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from app.core.config import settings
from app.core.exceptions import LLMError


class LLMService:
    """Service responsible for interacting with the LLM."""

    def __init__(self) -> None:
        self.llm = OllamaLLM(
            model=settings.models.llm_model,
            temperature=0,
            num_ctx=1024,
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, say:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""
        )

        self.chain = self.prompt | self.llm

    def generate_answer(
        self,
        question: str,
        context: str,
    ) -> str:
        """Generate an answer using the retrieved context."""

        try:
            return self.chain.invoke(
                {
                    "context": context,
                    "question": question,
                }
            )

        except Exception as exc:
            raise LLMError("Failed to generate an answer.") from exc
