from pathlib import Path
from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings

def load_text(file_path: str) -> str:
    return Path(file_path).read_text()

def split_text(text: str) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    return splitter.create_documents([text])

def create_vectorstore(documents: List[Document]) -> Chroma:
    embeddings = OllamaEmbeddings(model="mistral")
    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings
    )

def query_vectorstore(vectorstore: Chroma, query: str, k: int = 3) -> List[Document]:
    return vectorstore.similarity_search(query, k=k)

def process_response(context_docs: List[Document], query: str, llm) -> str:
    context = "\n\n".join(doc.page_content for doc in context_docs)
    prompt = f"""
        Use the following context to answer the question. If you cannot answer from the context, say so.

        Context:
        {context}

        Question: {query}

        Answer:
    """
    return llm.invoke(prompt)

from pathlib import Path

# At module level


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).parent.parent  # Gets us to root litrag/ project directory
    FIXTURES_DIR = PROJECT_ROOT / "data" / "fixtures"
    from litrag.llm import get_llm
    
    text = load_text(FIXTURES_DIR / "sample_story.txt")
    docs = split_text(text)
    vectorstore = create_vectorstore(docs)
    
    llm = get_llm()
    while True:
        query = input("\nEnter query (or 'quit'): ")
        if query.lower() == 'quit':
            break
            
        context_docs = query_vectorstore(vectorstore, query)
        response = process_response(context_docs, query, llm)
        print(f"\nResponse: {response}")