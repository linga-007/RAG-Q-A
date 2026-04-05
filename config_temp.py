import os

PINECONE_API_KEY = "PINECONE_API_KEY"
PINECONE_ENV = "PINECONE_ENV"
INDEX_NAME = "INDEX_NAME"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2" # you can choose any other embedding models

CHUNK_SIZE = 500 # you can adjust this based on your needs and the typical length of your documents
CHUNK_OVERLAP = 50 # overlap helps to maintain context across chunks, especially for longer documents

TOP_K = 5 # number of relevant chunks to retrieve for each query, can be tuned based on your use case

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b" # use model according to your need