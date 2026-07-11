from agent.retrieval_wrapper import RetrievalWrapper
import json, os

def test_retrieval_returns_docs(tmp_path):
    rw = RetrievalWrapper(persist_dir=str(tmp_path))
    doc = {"doc_id": "contract_test", "type": "SLA", "clause": "Delivery within 24h"}
    rw.add_doc(doc)
    hits = rw.query("delivery")
    assert any(h["doc_id"] == "contract_test" for h in hits)
