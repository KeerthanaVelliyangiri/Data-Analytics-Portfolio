import streamlit as st
from ai.llm_provider import get_llm, provider_status
from recruiter.screening import screen_resumes
from recruiter.candidate_filters import filter_candidates
from recruiter.recruiter_chat import answer_recruiter_question
from job_seeker.resume_analysis import analyze_for_job_seeker
from job_seeker.skill_gap import build_skill_gap
from job_seeker.career_roadmap import build_roadmap
from job_seeker.mock_interview import generate_questions, evaluate_answer
from job_seeker.job_search import job_search_links
from rag.resume_validator import validate_resume
from rag.document_loader import extract_text
from database.db import init_db, save_report

st.set_page_config(page_title="ResumeSync | AI Career & Recruitment", page_icon="🎯", layout="wide")
init_db()

st.title("🎯 ResumeSync")
st.caption("AI Career & Recruitment Intelligence Platform")
with st.sidebar:
    st.header("Workspace")
    mode = st.radio("Choose a mode", ["Recruiter Mode", "Job Seeker Mode"])
    workspace = st.text_input("Workspace / session ID", value="default", help="Use a unique ID for each recruiter or job seeker. Do not share IDs.")
    st.caption("AI provider: " + provider_status())
    st.divider()
    st.caption("AI results are decision-support only. Review source evidence before making hiring decisions.")

llm = get_llm()
if llm is None:
    st.warning("Add GEMINI_API_KEY and/or GROQ_API_KEY in Streamlit secrets or environment variables to enable AI analysis. Document extraction and validation still work.")

if mode == "Recruiter Mode":
    st.header("Recruiter workspace")
    jd = st.text_area("Paste the job description", height=180, placeholder="Role, responsibilities, required skills, qualification and experience...")
    uploads = st.file_uploader("Upload candidate resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)
    if st.button("Validate and screen candidates", type="primary", disabled=not (jd.strip() and uploads)):
        results, rejected = screen_resumes(uploads, jd, llm, workspace)
        st.session_state["candidate_results"] = results
        st.session_state["rejected_files"] = rejected
        for r in results:
            save_report(workspace, "recruiter", r.get("candidate_name", "Unknown"), r)
    for item in st.session_state.get("rejected_files", []):
        st.error(item)
    results = st.session_state.get("candidate_results", [])
    if results:
        st.subheader("Candidate comparison")
        filtered = filter_candidates(results)
        st.dataframe([{k: r.get(k) for k in ["candidate_name", "qualification", "experience_level", "location", "match_percentage", "recommendation"]} for r in filtered], use_container_width=True)
        for r in filtered:
            with st.expander(f"{r.get('candidate_name','Candidate')} — {r.get('match_percentage',0)}% match"):
                st.write("**Matched skills:**", ", ".join(r.get("matched_skills", [])) or "Not identified")
                st.write("**Missing skills:**", ", ".join(r.get("missing_skills", [])) or "Not identified")
                st.write("**Strengths:**", r.get("strengths", []))
                st.write("**Concerns:**", r.get("weaknesses", []))
                st.write("**Evidence:**", r.get("evidence", []))
                st.write("**Summary:**", r.get("overall_assessment", ""))
        st.subheader("Ask questions about these candidates")
        question = st.text_input("Example: Which candidates have Python and SQL?")
        if st.button("Ask recruiter assistant", disabled=not question.strip()):
            st.write(answer_recruiter_question(question, results, llm))
        csv_rows = [{"candidate_name":r.get("candidate_name"),"qualification":r.get("qualification"),"experience_level":r.get("experience_level"),"location":r.get("location"),"match_percentage":r.get("match_percentage"),"recommendation":r.get("recommendation")} for r in results]
        import pandas as pd
        st.download_button("Download candidate comparison CSV", pd.DataFrame(csv_rows).to_csv(index=False), "resumesync_candidates.csv", "text/csv")

else:
    st.header("Job seeker workspace")
    upload = st.file_uploader("Upload your resume", type=["pdf", "docx"], accept_multiple_files=False)
    jd = st.text_area("Paste your target job description", height=160)
    if st.button("Analyse my resume", type="primary", disabled=not (upload and jd.strip())):
        text, error = extract_text(upload)
        if error:
            st.error(error)
        else:
            valid, reason = validate_resume(text)
            if not valid:
                st.error(reason)
            elif llm is None:
                st.error("Configure an AI API key before running the analysis.")
            else:
                report = analyze_for_job_seeker(text, jd, llm)
                if report:
                    st.session_state["job_report"] = report
                    st.session_state["job_resume_text"] = text
                    save_report(workspace, "job_seeker", report.get("candidate_name", "Job seeker"), report)
    report = st.session_state.get("job_report")
    if report:
        st.subheader("Your match report")
        st.metric("Estimated job match", f"{report.get('match_percentage', 0)}%")
        c1, c2 = st.columns(2)
        with c1:
            st.write("**Matched skills**", report.get("matched_skills", []))
            st.write("**Missing skills**", report.get("missing_skills", []))
        with c2:
            st.write("**Strengths**", report.get("strengths", []))
            st.write("**Improvement areas**", report.get("weaknesses", []))
        st.write("**Assessment**", report.get("overall_assessment", ""))
        if st.button("Create skill-gap plan"):
            st.session_state["skill_gap"] = build_skill_gap(report, llm)
        if "skill_gap" in st.session_state:
            st.subheader("Skill-gap recommendations")
            st.write(st.session_state["skill_gap"])
        if st.button("Create 8-week career roadmap"):
            st.session_state["roadmap"] = build_roadmap(report, llm)
        if "roadmap" in st.session_state:
            st.subheader("Career roadmap")
            st.write(st.session_state["roadmap"])
        st.subheader("Job search links")
        st.caption("These are live search links, not verified individual vacancies.")
        job_role = st.text_input("Target job title", value="Data Analyst")
        job_location = st.text_input("Preferred job location", value="Coimbatore, India")
        for label, url in job_search_links(job_role, job_location):
            st.markdown(f"- [{label}]({url})")
        st.subheader("Mock interview practice")
        if st.button("Generate interview questions"):
            st.session_state["interview_questions"] = generate_questions(report, jd, llm)
        questions = st.session_state.get("interview_questions", [])
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}. {q}**")
            ans = st.text_area("Your answer", key=f"answer_{i}")
            if st.button("Get feedback", key=f"feedback_{i}", disabled=not ans.strip()):
                st.write(evaluate_answer(q, ans, llm))

st.divider()
st.caption("ResumeSync prototype • Keep API keys private • Candidate data is scoped by workspace ID.")
