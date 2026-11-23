
import json
import re

from ai.prompts import RESUME_ANALYSIS_PROMPT
from rag.document_loader import extract_text
from rag.resume_validator import validate_resume
from rag.text_splitter import split_text


def _clean_response(raw):
    """Convert an AI response into plain text."""

    if isinstance(raw, list):
        parts = []

        for item in raw:
            if isinstance(item, dict):
                parts.append(str(item.get("text", "")))
            else:
                parts.append(str(item))

        raw = "\n".join(parts)

    return str(raw).strip()


def _parse_json(raw):
    """Extract and validate JSON returned by Gemini or Groq."""

    raw = _clean_response(raw)

    if not raw:
        raise ValueError("AI returned an empty response.")

    # Remove Markdown code fences.
    raw = re.sub(
        r"```(?:json)?\s*",
        "",
        raw,
        flags=re.IGNORECASE
    )
    raw = raw.replace("```", "").strip()

    # Find the JSON object.
    start = raw.find("{")

    if start == -1:
        raise ValueError("AI response did not contain a JSON object.")

    # Decode one JSON object, even if extra text follows it.
    try:
        data, _ = json.JSONDecoder().raw_decode(raw[start:])
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"AI returned invalid JSON: {exc}"
        )

    if not isinstance(data, dict):
        raise ValueError("AI response must be a JSON object.")

    # Make sure the AI returned some actual analysis.
    meaningful_fields = [
        "candidate_name",
        "matched_skills",
        "missing_skills",
        "match_percentage",
        "overall_assessment",
        "recommendation",
        "technical_skills",
        "strengths"
    ]

    if not any(key in data for key in meaningful_fields):
        raise ValueError("AI returned an empty or incomplete analysis.")

    # Fill missing fields with safe defaults.
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
        "overall_assessment": "Assessment not provided.",
        "strengths": [],
        "weaknesses": [],
        "recommendation": "Review"
    }

    for key, default_value in defaults.items():
        if key not in data or data[key] is None:
            data[key] = default_value

    # Ensure list fields always contain lists.
    list_fields = [
        "technical_skills",
        "soft_skills",
        "matched_skills",
        "missing_skills",
        "strengths",
        "weaknesses"
    ]

    for field in list_fields:
        value = data[field]

        if isinstance(value, str):
            data[field] = [value] if value.strip() else []
        elif isinstance(value, list):
            data[field] = value
        else:
            data[field] = []

    # Safely convert match percentage into a number.
    try:
        percentage = str(data["match_percentage"])
        percentage = percentage.replace("%", "").strip()

        percentage = float(percentage)

        data["match_percentage"] = max(
            0,
            min(100, round(percentage))
        )

    except (ValueError, TypeError):
        data["match_percentage"] = 0

    # Ensure text fields contain strings.
    text_fields = [
        "candidate_name",
        "email",
        "phone",
        "qualification",
        "experience",
        "overall_assessment",
        "recommendation"
    ]

    for field in text_fields:
        if not isinstance(data[field], str):
            data[field] = str(data[field])

    # Normalize recommendation.
    recommendation = data["recommendation"].strip().lower()

    if "shortlist" in recommendation:
        data["recommendation"] = "Shortlist"
    elif "not recommended" in recommendation:
        data["recommendation"] = "Not Recommended"
    else:
        data["recommendation"] = "Review"

    return data


def screen_resumes(uploads, jd, llm, workspace):

    results = []
    rejected = []

    # Check AI provider.
    if llm is None:
        return [], [
            "AI provider is not configured. "
            "Add a Gemini or Groq API key."
        ]

    # Check job description.
    if not jd or not jd.strip():
        return [], ["Please provide a job description."]

    if not uploads:
        return [], ["Please upload at least one resume."]

    for upload in uploads:

        try:
            # Step 1: Extract document text.
            text, error = extract_text(upload)

            if error:
                rejected.append(
                    f"{upload.name}: {error}"
                )
                continue

            if not text or not text.strip():
                rejected.append(
                    f"{upload.name}: No readable text found."
                )
                continue

            # Step 2: Validate whether document is a resume.
            valid, reason = validate_resume(text)

            if not valid:
                rejected.append(
                    f"{upload.name}: {reason}"
                )
                continue

            # Step 3: Create the AI prompt.
            prompt = RESUME_ANALYSIS_PROMPT.format(
                jd=jd,
                resume=text[:24000]
            )

            # Step 4: Get AI response.
            response = llm.invoke(prompt)

            raw_response = response.content

            # Step 5: Parse and validate the AI response.
            result = _parse_json(raw_response)

            # Step 6: Add source information.
            result["source_file"] = upload.name
            result["workspace"] = workspace
            result["resume_chunks"] = split_text(text)

            # Step 7: Add only successful candidates.
            results.append(result)

        except Exception as exc:

            rejected.append(
                f"{upload.name}: Analysis failed; "
                f"candidate was not added. Details: {exc}"
            )

    return results, rejected
