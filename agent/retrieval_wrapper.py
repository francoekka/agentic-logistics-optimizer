import os
import json
from typing import List, Dict
from chromadb import Client
from chromadb.config import Settings

# Simple hybrid retrieval wrapper (vector + keyword)
class RetrievalWrapper:
    def __init__(self, persist_dir="rag-corpus-index"):
        self.client = Client(Settings(persist_directory=persist_dir))
        self.collection = self.client.get_or_create_collection("logistics_docs")

    def add_doc(self, doc: Dict):
        self.collection.add(
            documents=[doc["clause"] if "clause" in doc else doc.get("summary", doc.get("rule", ""))],
            metadatas=[{"doc_id": doc["doc_id"], "type": doc["type"]}],
            ids=[doc["doc_id"]]
        )

    def query(self, text: str, top_k: int = 3) -> List[Dict]:
        results = self.collection.query(query_texts=[text], n_results=top_k)
        return [
            {"doc_id": md["doc_id"], "type": md["type"], "content": doc}
            for doc, md in zip(results["documents"][0], results["metadatas"][0])
        ]


if __name__ == "__main__":
    rw = RetrievalWrapper()
    # Seed docs from rag-corpus
    for folder in ["contracts", "incidents", "policies"]:
        path = os.path.join("rag-corpus", folder)
        for fname in os.listdir(path):
            with open(os.path.join(path, fname)) as f:
                rw.add_doc(json.load(f))

    # Query example
    hits = rw.query("delivery delay penalties")
    print("Retrieved docs:", hits)
