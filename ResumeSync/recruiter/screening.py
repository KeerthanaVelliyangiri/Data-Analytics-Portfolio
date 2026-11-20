import json, re
from ai.prompts import RESUME_ANALYSIS_PROMPT
from rag.document_loader import extract_text
from rag.resume_validator import validate_resume
from rag.text_splitter import split_text


def _parse_json(raw):
    raw = str(raw).strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.I)
    start, end = raw.find("{"), raw.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("AI response did not contain a JSON object")
    data = json.loads(raw[start:end+1])
    required = ["candidate_name", "matched_skills", "missing_skills", "match_percentage", "overall_assessment", "recommendation"]
    if any(key not in data for key in required):
        raise ValueError("AI response is missing required fields")
    if not isinstance(data["matched_skills"], list) or not isinstance(data["missing_skills"], list):
        raise ValueError("Skills fields must be lists")
    data["match_percentage"] = max(0, min(100, int(float(data["match_percentage"]))))
    return data


def screen_resumes(uploads, jd, llm, workspace):
    results, rejected = [], []
    if llm is None:
        return [], ["AI provider is not configured. Add a Gemini or Groq API key."]
    for upload in uploads:
        text, error = extract_text(upload)
        if error:
            rejected.append(f"{upload.name}: {error}"); continue
        valid, reason = validate_resume(text)
        if not valid:
            rejected.append(f"{upload.name}: {reason}"); continue
        try:
            prompt = RESUME_ANALYSIS_PROMPT.format(jd=jd, resume=text[:24000])
            response = llm.invoke(prompt).content
            result = _parse_json(response)
            result["source_file"] = upload.name
            result["workspace"] = workspace
            result["resume_chunks"] = split_text(text)
            results.append(result)
        except Exception as exc:
            rejected.append(f"{upload.name}: Analysis failed; candidate was not added. Details: {exc}")
    return results, rejected
