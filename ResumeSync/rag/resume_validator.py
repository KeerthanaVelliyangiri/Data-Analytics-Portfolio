import re

RESUME_SECTIONS = [
    r"\b(education|academic background|qualification)\b",
    r"\b(experience|employment|work history|internship)\b",
    r"\b(skills|technical skills|technologies)\b",
    r"\b(projects|personal projects|academic projects)\b",
    r"\b(certifications|courses|achievements)\b",
    r"\b(contact|email|phone|linkedin|github)\b",
]
NON_RESUME_HINTS = [r"\binvoice\b", r"\bsubtotal\b", r"\btax invoice\b", r"\brestaurant menu\b", r"\bmenu items\b", r"\btable of contents\b"]


def validate_resume(text: str):
    if not text or len(text.strip()) < 120:
        return False, "Very little text was extracted. This may be a scanned PDF or an empty document. Try a text-based PDF/DOCX; OCR can be added separately."
    normalized = re.sub(r"\s+", " ", text.lower())
    sections = sum(bool(re.search(pattern, normalized)) for pattern in RESUME_SECTIONS)
    has_contact = bool(re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|\b\+?\d[\d ()-]{7,}\d\b|\blinkedin\b", normalized))
    has_profile = bool(re.search(r"\b(resume|curriculum vitae|career objective|professional summary|profile)\b", normalized))
    non_resume = sum(bool(re.search(pattern, normalized)) for pattern in NON_RESUME_HINTS)
    if non_resume >= 2 and sections < 2:
        return False, "This document looks like an invoice, menu or another non-resume document. Please upload a candidate resume."
    if sections < 2 or not (has_contact or has_profile):
        return False, "This document could not be confidently identified as a resume. Include sections such as Education, Skills, Experience or Projects and contact/profile details."
    return True, "Resume validation passed."
