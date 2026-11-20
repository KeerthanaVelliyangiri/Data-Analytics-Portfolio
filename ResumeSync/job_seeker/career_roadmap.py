def build_roadmap(report, llm):
    prompt = f"Create an achievable 8-week learning roadmap for this target role. Include weekly goals, topics, one practical exercise and a measurable outcome. Assume beginner-to-intermediate level unless resume evidence says otherwise. Missing skills: {report.get('missing_skills', [])}. Matched skills: {report.get('matched_skills', [])}."
    return llm.invoke(prompt).content
