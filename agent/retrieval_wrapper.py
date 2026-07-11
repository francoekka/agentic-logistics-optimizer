import os
import json

class RetrievalWrapper:
    def __init__(self, persist_dir="index"):
        self.persist_dir = persist_dir
        os.makedirs(self.persist_dir, exist_ok=True)
        self.docs = []

    def add_doc(self, doc):
        self.docs.append(doc)

    def query(self, text):
        # naive keyword search
        return [d for d in self.docs if text.lower() in json.dumps(d).lower()]
