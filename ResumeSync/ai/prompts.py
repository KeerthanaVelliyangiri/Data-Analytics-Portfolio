
RESUME_ANALYSIS_PROMPT = """
You are an expert resume analysis assistant.

Analyze the candidate's resume against the given job description.

JOB DESCRIPTION:
{jd}

RESUME:
{resume}

Instructions:
1. Extract candidate information from the resume.
2. Identify technical and soft skills.
3. Identify matched skills.
4. Identify missing skills.
5. Evaluate qualification and experience.
6. Calculate a reasonable match percentage based on evidence.
7. Explain the candidate's strengths and weaknesses.
8. Provide improvement recommendations.
9. Do not invent information that is not present in the resume.
10. If information is unavailable, use "Not specified".

Return ONLY valid JSON using this structure:

{{
    "candidate_name": "Candidate name or Not specified",
    "email": "Email or Not specified",
    "phone": "Phone or Not specified",
    "qualification": "Qualification or Not specified",
    "experience": "Experience or Not specified",
    "technical_skills": [],
    "soft_skills": [],
    "matched_skills": [],
    "missing_skills": [],
    "match_percentage": 0,
    "overall_assessment": "Assessment",
    "strengths": [],
    "weaknesses": [],
    "recommendation": "Shortlist or Review or Not Recommended"
}}

Important:
- Use double quotes for JSON keys and string values.
- Do not add Markdown code fences.
- Do not add explanations outside JSON.
- match_percentage must be a number between 0 and 100.
- All list fields must be JSON arrays.
- Never invent candidate details.
"""


