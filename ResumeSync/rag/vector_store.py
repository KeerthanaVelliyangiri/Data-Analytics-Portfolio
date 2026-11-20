from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from rag.embeddings import get_embeddings


def build_candidate_store(candidates):
    docs = []
    for candidate in candidates:
        for chunk in candidate.get("resume_chunks", []):
            docs.append(Document(page_content=chunk, metadata={"candidate_name": candidate.get("candidate_name", "Unknown"), "workspace": candidate.get("workspace", "") }))
    if not docs:
        return None
    return FAISS.from_documents(docs, get_embeddings())
