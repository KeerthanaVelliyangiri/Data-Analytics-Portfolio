import json, re
from ai.prompts import RESUME_ANALYSIS_PROMPT


def analyze_for_job_seeker(resume, jd, llm):
    prompt = RESUME_ANALYSIS_PROMPT.format(jd=jd, resume=resume[:24000])
    raw = str(llm.invoke(prompt).content).strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.I)
    data = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
    if "match_percentage" not in data or "matched_skills" not in data or "missing_skills" not in data:
        raise ValueError("AI response did not include the required match fields")
    data["match_percentage"] = max(0, min(100, int(float(data["match_percentage"]))))
    return data
