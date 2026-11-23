
import json
import re
from ai.prompts import RESUME_ANALYSIS_PROMPT


def _clean_response(raw):
    """Clean the AI response before parsing JSON."""
    if isinstance(raw, list):
        raw = " ".join(str(item) for item in raw)

    raw = str(raw).strip()

    # Remove Markdown JSON code fences
    raw = re.sub(
        r"^```(?:json)?\s*|\s*```$",
        "",
        raw,
        flags=re.IGNORECASE
    )

    return raw.strip()


def _parse_job_seeker_json(raw):
    """Safely parse the AI response and fill missing fields."""
    raw = _clean_response(raw)

    start = raw.find("{")

    if start == -1:
        raise ValueError("AI response did not contain a JSON object")

    try:
        data, _ = json.JSONDecoder().raw_decode(raw[start:])
    except json.JSONDecodeError as exc:
        raise ValueError(f"AI returned invalid JSON: {exc}")

    if not isinstance(data, dict):
        raise ValueError("AI response must be a JSON object")

    # Default values for missing fields
    defaults = {
        "candidate_name": "Not specified",
        "email": "Not specified",
        "phone": "Not specified",
        "qualification": "Not specified",
        "experience": "Not specified",
        "technical_skills": [],
        "soft_skills": [],
        "matched_skills": [],
        "missing_skills": [],
        "match_percentage": 0,
        "overall_assessment": "Assessment not available",
        "strengths": [],
        "weaknesses": [],
        "recommendation": "Review"
    }

    for key, default_value in defaults.items():
        if key not in data or data[key] is None:
            data[key] = default_value

    # Ensure skill and feedback fields are lists
    list_fields = [
        "technical_skills",
        "soft_skills",
        "matched_skills",
        "missing_skills",
        "strengths",
        "weaknesses"
    ]

    for field in list_fields:
        if not isinstance(data[field], list):
            data[field] = [str(data[field])] if data[field] else []

    # Safely convert match percentage
    try:
        percentage = float(data["match_percentage"])
        data["match_percentage"] = max(0, min(100, int(percentage)))
    except (ValueError, TypeError):
        data["match_percentage"] = 0

    return data


def analyze_for_job_seeker(resume, jd, llm):
    """Analyze one resume against a job description."""

    if llm is None:
        raise ValueError("AI provider is not configured.")

    if not resume or not resume.strip():
        raise ValueError("Resume text is empty.")

    if not jd or not jd.strip():
        raise ValueError("Please provide a job description.")

    prompt = RESUME_ANALYSIS_PROMPT.format(
        jd=jd,
        resume=resume[:24000]
    )

    response = llm.invoke(prompt)

    print("\n========== RAW RESPONSE ==========")
    print(repr(response.content))
    print("========== END RESPONSE ==========\n")

    return _parse_job_seeker_json(response.content)  
