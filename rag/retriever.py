from rag.embedder import get_embedding
from config import TOP_K

def retrieve(query, db):
    query_embedding = get_embedding(query)
    return db.search(query_embedding , TOP_K)