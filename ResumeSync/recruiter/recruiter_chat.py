from rag.retriever import retrieve_candidate_evidence


def answer_recruiter_question(question, candidates, llm):
    if llm is None:
        return "Configure an AI provider first."
    try:
        docs = retrieve_candidate_evidence(question, candidates, k=6)
        evidence = "\n\n".join(f"Candidate: {d.metadata.get('candidate_name')}\nEvidence: {d.page_content}" for d in docs)
        if not evidence:
            return "No matching resume evidence was found in the currently loaded candidates."
        prompt = f"Answer only from the resume evidence below. Name candidates. If evidence is insufficient, say so. Do not infer missing skills.\nQUESTION: {question}\nEVIDENCE:\n{evidence}"
        return llm.invoke(prompt).content
    except Exception as exc:
        return f"Could not retrieve evidence: {exc}"
