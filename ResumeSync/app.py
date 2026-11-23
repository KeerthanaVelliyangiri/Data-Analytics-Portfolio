
import uuid
import pandas as pd
import streamlit as st

from ai.llm_provider import get_llm

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


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ResumeSync | AI Career & Recruitment",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_db()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "current_mode" not in st.session_state:
    st.session_state.current_mode = "Recruiter Mode"

if "recruiter_workspace_id" not in st.session_state:
    st.session_state.recruiter_workspace_id = (
        "recruiter_" + uuid.uuid4().hex
    )

if "job_seeker_workspace_id" not in st.session_state:
    st.session_state.job_seeker_workspace_id = (
        "job_seeker_" + uuid.uuid4().hex
    )


def clear_recruiter_data():
    keys = [
        "candidate_results",
        "rejected_files",
        "recruiter_question",
        "recruiter_answer"
    ]

    for key in keys:
        st.session_state.pop(key, None)


def clear_job_seeker_data():
    keys = [
        "job_report",
        "job_resume_text",
        "skill_gap",
        "roadmap",
        "interview_questions",
        "interview_feedback"
    ]

    for key in keys:
        st.session_state.pop(key, None)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f7f8fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1600px;
    }

    h1 {
        font-size: 38px !important;
        font-weight: 800 !important;
        color: #172554 !important;
    }

    h2 {
        font-size: 30px !important;
        font-weight: 750 !important;
        color: #172554 !important;
    }

    h3 {
        font-size: 23px !important;
        font-weight: 700 !important;
        color: #1e293b !important;
    }

    p, label, li {
        font-size: 17px !important;
        line-height: 1.7 !important;
    }

    /* Sidebar */

    [data-testid="stSidebar"] {
        background-color: #f0f3fa;
        min-width: 300px;
    }

    [data-testid="stSidebar"] h2 {
        font-size: 27px !important;
        font-weight: 800 !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        font-size: 17px !important;
    }

    textarea {
        font-size: 16px !important;
        line-height: 1.6 !important;
    }

    /* Buttons */

    div.stButton > button {
        min-height: 45px;
        font-size: 16px;
        font-weight: 650;
        border-radius: 8px;
        padding: 8px 22px;
    }

    /* Metrics */

    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
    }

    [data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: 750;
    }

    /* Hero banner */

    .hero-banner {
        background: linear-gradient(120deg, #172554, #2563eb);
        padding: 35px 40px;
        border-radius: 16px;
        margin-bottom: 30px;
        color: white;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 850;
        color: white;
        margin: 0;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 19px;
        color: #dbeafe;
        margin-top: 10px;
        margin-bottom: 0;
    }

    hr {
        margin-top: 25px;
        margin-bottom: 25px;
        border-color: #dbe2ef;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="hero-banner">
        <div class="hero-title">ResumeSync</div>
        <div class="hero-subtitle">
            AI Career and Recruitment Intelligence Platform
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## Workspace")

    mode = st.radio(
        "Choose a mode",
        ["Recruiter Mode", "Job Seeker Mode"],
        key="mode_selector"
    )


# --------------------------------------------------
# CLEAR PREVIOUS MODE RESULTS
# --------------------------------------------------

previous_mode = st.session_state.current_mode

if mode != previous_mode:

    if mode == "Recruiter Mode":
        clear_job_seeker_data()

    else:
        clear_recruiter_data()

    st.session_state.current_mode = mode


# --------------------------------------------------
# AI PROVIDER
# --------------------------------------------------

llm = get_llm()

if llm is None:
    st.warning(
        "AI provider is unavailable. Please configure your API key."
    )


# ==================================================
# RECRUITER MODE
# ==================================================

if mode == "Recruiter Mode":

    st.markdown("## Recruiter Workspace")

    st.write(
        "Upload candidate resumes and evaluate their "
        "qualifications against your job requirements."
    )

    st.divider()

    # Job description

    st.markdown("### Job Description")

    jd = st.text_area(
        "Paste the job description",
        height=190,
        placeholder=(
            "Enter the job role, responsibilities, "
            "required skills, qualification and experience..."
        ),
        key="recruiter_jd"
    )

    # Resume upload

    st.markdown("### Upload Candidate Resumes")

    uploads = st.file_uploader(
        "Upload PDF or DOCX resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True,
        key="recruiter_uploads"
    )

    # Screen candidates

    if st.button(
        "Validate and Screen Candidates",
        type="primary",
        disabled=not (jd.strip() and uploads)
    ):

        if llm is None:

            st.error("AI provider is unavailable.")

        else:

            with st.spinner("Analyzing candidate resumes..."):

                results, rejected = screen_resumes(
                    uploads,
                    jd,
                    llm,
                    st.session_state.recruiter_workspace_id
                )

                st.session_state["candidate_results"] = results
                st.session_state["rejected_files"] = rejected

                for result in results:

                    save_report(
                        st.session_state.recruiter_workspace_id,
                        "recruiter",
                        result.get("candidate_name", "Unknown"),
                        result
                    )

            if results:
                st.success(
                    f"Successfully analyzed {len(results)} candidate(s)."
                )
            else:
                st.warning("No candidates were successfully analyzed.")

    # Rejected files

    for item in st.session_state.get("rejected_files", []):
        st.error(item)

    # Candidate results

    results = st.session_state.get("candidate_results", [])

    if results:

        st.divider()

        st.markdown("## Candidate Comparison")

        filtered = filter_candidates(results)

        if filtered:

            comparison_rows = []

            for result in filtered:

                comparison_rows.append({
                    "Candidate Name": result.get(
                        "candidate_name", "Not specified"
                    ),
                    "Qualification": result.get(
                        "qualification", "Not specified"
                    ),
                    "Experience": result.get(
                        "experience_level",
                        result.get("experience", "Not specified")
                    ),
                    "Location": result.get(
                        "location", "Not specified"
                    ),
                    "Match %": result.get("match_percentage", 0),
                    "Recommendation": result.get(
                        "recommendation", "Review"
                    )
                })

            comparison_df = pd.DataFrame(comparison_rows)

            st.dataframe(
                comparison_df,
                use_container_width=True,
                hide_index=True
            )

            # Candidate details

            st.markdown("## Candidate Details")

            for result in filtered:

                candidate_name = result.get(
                    "candidate_name", "Candidate"
                )

                match_score = result.get("match_percentage", 0)

                with st.expander(
                    f"{candidate_name} | {match_score}% Match"
                ):

                    col1, col2 = st.columns(2)

                    with col1:

                        st.markdown("### Candidate Information")

                        st.write(
                            "**Name:**",
                            candidate_name
                        )

                        st.write(
                            "**Email:**",
                            result.get("email", "Not specified")
                        )

                        st.write(
                            "**Phone:**",
                            result.get("phone", "Not specified")
                        )

                        st.write(
                            "**Qualification:**",
                            result.get("qualification", "Not specified")
                        )

                        st.write(
                            "**Experience:**",
                            result.get(
                                "experience_level",
                                result.get("experience", "Not specified")
                            )
                        )

                    with col2:

                        st.markdown("### Match Analysis")

                        st.metric(
                            "Estimated Match",
                            f"{match_score}%"
                        )

                        st.progress(
                            max(0, min(100, int(match_score))) / 100
                        )

                        st.write(
                            "**Recommendation:**",
                            result.get("recommendation", "Review")
                        )

                    st.divider()

                    skill_col1, skill_col2 = st.columns(2)

                    with skill_col1:

                        st.markdown("### Matched Skills")

                        matched = result.get("matched_skills", [])

                        if matched:
                            for skill in matched:
                                st.markdown(f"- {skill}")
                        else:
                            st.info("No matched skills identified.")

                    with skill_col2:

                        st.markdown("### Missing Skills")

                        missing = result.get("missing_skills", [])

                        if missing:
                            for skill in missing:
                                st.markdown(f"- {skill}")
                        else:
                            st.info("No missing skills identified.")

                    st.divider()

                    st.markdown("### Strengths")

                    strengths = result.get("strengths", [])

                    if strengths:
                        for item in strengths:
                            st.markdown(f"- {item}")
                    else:
                        st.write("Not specified.")

                    st.markdown("### Areas of Concern")

                    weaknesses = result.get("weaknesses", [])

                    if weaknesses:
                        for item in weaknesses:
                            st.markdown(f"- {item}")
                    else:
                        st.write("Not specified.")

                    st.markdown("### Evidence")

                    evidence = result.get("evidence", [])

                    if evidence:
                        for item in evidence:
                            st.markdown(f"- {item}")
                    else:
                        st.write("No evidence provided by the AI.")

                    st.markdown("### Overall Assessment")

                    st.write(
                        result.get(
                            "overall_assessment",
                            "Assessment not available."
                        )
                    )

            # Recruiter assistant

            st.divider()

            st.markdown("## Recruiter Assistant")

            st.write(
                "Ask questions about the analyzed candidates."
            )

            question = st.text_input(
                "Your question",
                placeholder="Example: Which candidates have Python and SQL?",
                key="recruiter_question"
            )

            if st.button(
                "Ask Recruiter Assistant",
                disabled=not question.strip()
            ):

                if llm is None:
                    st.error("AI provider is unavailable.")

                else:

                    with st.spinner("Preparing the answer..."):

                        try:

                            answer = answer_recruiter_question(
                                question,
                                results,
                                llm
                            )

                            st.session_state["recruiter_answer"] = answer

                        except Exception as exc:

                            st.error(
                                f"Unable to answer the question: {exc}"
                            )

            if st.session_state.get("recruiter_answer"):

                st.markdown("### Assistant Response")

                st.write(
                    st.session_state["recruiter_answer"]
                )

            # CSV download

            st.divider()

            st.markdown("## Export Candidate Comparison")

            csv_data = comparison_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "Download Candidate Comparison CSV",
                data=csv_data,
                file_name="resumesync_candidates.csv",
                mime="text/csv"
            )

        else:

            st.info(
                "No candidates match the selected filter criteria."
            )


# ==================================================
# JOB SEEKER MODE
# ==================================================

else:

    st.markdown("## Job Seeker Workspace")

    st.write(
        "Analyze your resume, identify skill gaps "
        "and discover opportunities to improve your career."
    )

    st.divider()

    # Resume upload

    st.markdown("### Upload Your Resume")

    upload = st.file_uploader(
        "Upload your resume in PDF or DOCX format",
        type=["pdf", "docx"],
        accept_multiple_files=False,
        key="job_seeker_upload"
    )

    # Job description

    st.markdown("### Target Job Description")

    jd = st.text_area(
        "Paste your target job description",
        height=190,
        placeholder="Paste the job description here...",
        key="job_seeker_jd"
    )

    # Analyze resume

    if st.button(
        "Analyze My Resume",
        type="primary",
        disabled=not (upload and jd.strip())
    ):

        with st.spinner("Analyzing your resume..."):

            text, error = extract_text(upload)

            if error:

                st.error(error)

            else:

                valid, reason = validate_resume(text)

                if not valid:

                    st.error(reason)

                elif llm is None:

                    st.error(
                        "Configure an AI API key before running the analysis."
                    )

                else:

                    try:

                        report = analyze_for_job_seeker(
                            text,
                            jd,
                            llm
                        )

                        st.session_state["job_report"] = report
                        st.session_state["job_resume_text"] = text

                        for key in [
                            "skill_gap",
                            "roadmap",
                            "interview_questions",
                            "interview_feedback"
                        ]:
                            st.session_state.pop(key, None)

                        save_report(
                            st.session_state.job_seeker_workspace_id,
                            "job_seeker",
                            report.get("candidate_name", "Job Seeker"),
                            report
                        )

                        st.success("Your resume analysis is complete.")

                    except Exception as exc:

                        st.error(
                            f"Resume analysis failed: {exc}"
                        )

    # Display report

    report = st.session_state.get("job_report")

    if report:

        st.divider()

        st.markdown("## Your Career Analysis Report")

        st.caption(
            "AI-powered resume and job description comparison"
        )

        # Match score and assessment

        score_col, assessment_col = st.columns([1, 2])

        match_score = report.get("match_percentage", 0)

        with score_col:

            st.metric(
                "Estimated Job Match",
                f"{match_score}%"
            )

            st.progress(
                max(0, min(100, int(match_score))) / 100
            )

        with assessment_col:

            st.markdown("### Overall Assessment")

            st.write(
                report.get(
                    "overall_assessment",
                    "Assessment not available."
                )
            )

        st.divider()

        # Skills

        st.markdown("## Skills Analysis")

        matched_col, missing_col = st.columns(2)

        with matched_col:

            st.markdown("### Matched Skills")

            matched = report.get("matched_skills", [])

            if matched:
                for skill in matched:
                    st.markdown(f"- {skill}")
            else:
                st.info("No matched skills identified.")

        with missing_col:

            st.markdown("### Missing Skills")

            missing = report.get("missing_skills", [])

            if missing:
                for skill in missing:
                    st.markdown(f"- {skill}")
            else:
                st.info("No missing skills identified.")

        st.divider()

        # Strengths and weaknesses

        st.markdown("## Strengths and Improvement Areas")

        strength_col, improvement_col = st.columns(2)

        with strength_col:

            st.markdown("### Strengths")

            strengths = report.get("strengths", [])

            if strengths:
                for item in strengths:
                    st.markdown(f"- {item}")
            else:
                st.write("Not specified.")

        with improvement_col:

            st.markdown("### Improvement Areas")

            weaknesses = report.get("weaknesses", [])

            if weaknesses:
                for item in weaknesses:
                    st.markdown(f"- {item}")
            else:
                st.write("Not specified.")

        # Candidate information

        st.divider()

        st.markdown("## Resume Information")

        info_col1, info_col2 = st.columns(2)

        with info_col1:

            st.write(
                "**Candidate Name:**",
                report.get("candidate_name", "Not specified")
            )

            st.write(
                "**Email:**",
                report.get("email", "Not specified")
            )

            st.write(
                "**Phone:**",
                report.get("phone", "Not specified")
            )

        with info_col2:

            st.write(
                "**Qualification:**",
                report.get("qualification", "Not specified")
            )

            st.write(
                "**Experience:**",
                report.get("experience", "Not specified")
            )

            st.write(
                "**Recommendation:**",
                report.get("recommendation", "Review")
            )

        # Skill gap plan

        st.divider()

        st.markdown("## Skill Gap Recommendations")

        if st.button("Create Skill Gap Plan"):

            if llm is None:

                st.error("AI provider is unavailable.")

            else:

                with st.spinner("Creating your skill gap plan..."):

                    try:

                        st.session_state["skill_gap"] = build_skill_gap(
                            report,
                            llm
                        )

                    except Exception as exc:

                        st.error(
                            f"Unable to create skill gap plan: {exc}"
                        )

        if "skill_gap" in st.session_state:

            st.markdown("### Your Skill Gap Plan")

            st.write(st.session_state["skill_gap"])

        # Career roadmap

        st.divider()

        st.markdown("## Career Development Roadmap")

        if st.button("Create 8-Week Career Roadmap"):

            if llm is None:

                st.error("AI provider is unavailable.")

            else:

                with st.spinner("Preparing your career roadmap..."):

                    try:

                        st.session_state["roadmap"] = build_roadmap(
                            report,
                            llm
                        )

                    except Exception as exc:

                        st.error(
                            f"Unable to create career roadmap: {exc}"
                        )

        if "roadmap" in st.session_state:

            st.markdown("### Your 8-Week Roadmap")

            st.write(st.session_state["roadmap"])

        # Job search links

        st.divider()

        st.markdown("## Job Search")

        st.write(
            "Find relevant job opportunities using your preferred role and location."
        )

        job_col1, job_col2 = st.columns(2)

        with job_col1:

            job_role = st.text_input(
                "Target Job Title",
                value="Data Analyst",
                key="job_search_role"
            )

        with job_col2:

            job_location = st.text_input(
                "Preferred Job Location",
                value="Coimbatore, India",
                key="job_search_location"
            )

        if job_role.strip() and job_location.strip():

            for label, url in job_search_links(
                job_role,
                job_location
            ):

                st.markdown(f"- [{label}]({url})")

        st.caption(
            "These are job search links, not verified individual vacancies."
        )

        # Mock interview

        st.divider()

        st.markdown("## Mock Interview Practice")

        st.write(
            "Generate interview questions based on your resume "
            "and target job description."
        )

        if st.button("Generate Interview Questions"):

            if llm is None:

                st.error("AI provider is unavailable.")

            else:

                with st.spinner("Generating interview questions..."):

                    try:

                        st.session_state["interview_questions"] = (
                            generate_questions(report, jd, llm)
                        )

                        for key in list(st.session_state.keys()):
                            if key.startswith("interview_feedback_"):
                                st.session_state.pop(key, None)

                    except Exception as exc:

                        st.error(
                            f"Unable to generate questions: {exc}"
                        )

        questions = st.session_state.get(
            "interview_questions",
            []
        )

        for index, question in enumerate(questions):

            st.markdown(f"### Question {index + 1}")

            st.write(question)

            answer = st.text_area(
                "Your Answer",
                key=f"interview_answer_{index}",
                height=120
            )

            if st.button(
                "Get Feedback",
                key=f"feedback_button_{index}",
                disabled=not answer.strip()
            ):

                if llm is None:

                    st.error("AI provider is unavailable.")

                else:

                    with st.spinner("Evaluating your answer..."):

                        try:

                            feedback = evaluate_answer(
                                question,
                                answer,
                                llm
                            )

                            st.session_state[
                                f"interview_feedback_{index}"
                            ] = feedback

                        except Exception as exc:

                            st.error(
                                f"Unable to evaluate your answer: {exc}"
                            )

            feedback_key = f"interview_feedback_{index}"

            if feedback_key in st.session_state:

                st.markdown("#### Interview Feedback")

                st.write(st.session_state[feedback_key])
