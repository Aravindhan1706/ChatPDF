from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentProcessor:
    """Service responsible for processing PDF documents."""

    def extract_text(self, pdf_path: str) -> str:
        """Extract text from a PDF."""

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        return "\n".join(doc.page_content for doc in documents)

    def chunk_text(
        self,
        text: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> list[str]:
        """Split extracted text into chunks."""

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        return splitter.split_text(text)
