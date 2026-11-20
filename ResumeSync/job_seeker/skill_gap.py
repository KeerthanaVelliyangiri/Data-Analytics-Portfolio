def build_skill_gap(report, llm):
    prompt = f"Create a practical beginner-friendly skill-gap plan. Separate must-learn and optional skills. Suggest free/official learning sources where possible. Do not invent certifications.\nMatched: {report.get('matched_skills', [])}\nMissing: {report.get('missing_skills', [])}\nTarget assessment: {report.get('overall_assessment', '')}"
    return llm.invoke(prompt).content
