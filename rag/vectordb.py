from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY, PINECONE_ENV, INDEX_NAME

class VectorDB:
    def __init__(self, dimension):
        self.pc = Pinecone(api_key=PINECONE_API_KEY)

        # Create index if not exists
        if INDEX_NAME not in [i["name"] for i in self.pc.list_indexes()]:
            self.pc.create_index(
                name=INDEX_NAME,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region=PINECONE_ENV
                )
            )

        self.index = self.pc.Index(INDEX_NAME)

    def add(self, embeddings, texts):
        vectors = [
            {
                "id": str(i),
                "values": embeddings[i],
                "metadata": {"text": texts[i]}
            }
            for i in range(len(texts))
        ]

        self.index.upsert(vectors)

    def search(self, query_embedding, top_k=5):
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )

        return [match["metadata"]["text"] for match in results["matches"]]