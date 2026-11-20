from rag.vector_store import build_candidate_store


def retrieve_candidate_evidence(question, candidates, k=5):
    store = build_candidate_store(candidates)
    if store is None:
        return []
    return store.similarity_search(question, k=k)
