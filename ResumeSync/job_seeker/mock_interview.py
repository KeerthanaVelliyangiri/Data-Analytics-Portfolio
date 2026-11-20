import json, re


def generate_questions(report, jd, llm):
    prompt = f"Generate 8 concise interview questions based on this resume analysis and job description. Mix technical, HR and project questions. Return ONLY a JSON array of strings.\nANALYSIS: {json.dumps(report)}\nJOB: {jd[:6000]}"
    raw = str(llm.invoke(prompt).content).strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.I)
    data = json.loads(raw[raw.find("["):raw.rfind("]")+1])
    return [str(x) for x in data[:8]]


def evaluate_answer(question, answer, llm):
    prompt = f"Give kind, practical interview feedback. Assess correctness, clarity, structure and missing points. Then provide an improved sample answer. Do not claim facts about the candidate.\nQUESTION: {question}\nANSWER: {answer}"
    return llm.invoke(prompt).content
