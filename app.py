from rag.loader import load_pdf
from rag.chunker import chunk_docs
from rag.embedder import get_embedding
from rag.vectordb import VectorDB
from pathlib import Path
from rag.retriever import retrieve
from utils.helper import format_context
from prompts.prompt_template import build_prompt
from llm.llm_client import generate_response

def setup_pipeline(pdf_path):
    print("======================loading pdf======================")
    docs = load_pdf(pdf_path)

    print("======================chunking=============================")
    chunks = chunk_docs(docs)
    print(chunks)

    texts = [c.page_content for c in chunks]

    print("======================creating embeddings====================")
    embeddings = get_embedding(texts)
    print(embeddings)

    print("==========================storing in pinecone=============================")
    db = VectorDB(dimension = len(embeddings[0]))
    db.add(embeddings, texts)
    return db

def chat_loop(db):
    while(True):
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        mode = input("Mode (beginner/interview/summary): ")

        results = retrieve(query, db)
        print("===========================results=============================")
        print(results)
        context = format_context(results)
        print("===========================context=============================")

        print(context)

        prompt = build_prompt(context, query, mode)

        print("===========================prompt=============================")
        print(prompt)

        answer = generate_response( prompt)

        print("\nAnswer:\n", answer)

if(__name__ == "__main__"):
    pdf_path = Path(__file__).resolve().parent / "data" / "sample.pdf"
    db = setup_pipeline(str(pdf_path))
    chat_loop(db)