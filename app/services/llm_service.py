from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from app.core.config import settings


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

        print(f"Using model: {settings.models.llm_model}")

    def generate_answer(
        self,
        question: str,
        context: str,
    ) -> str:
        """Generate an answer using the retrieved context."""

        return self.chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )
