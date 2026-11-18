
import streamlit as st
import pandas as pd
import json
import re
import io
import time

from pypdf import PdfReader
from docx import Document

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)


# =====================================================
# 2. CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* Main application */
.stApp {
    background-color: #F4F7FB;
    color: #243247;
    font-family: 'Segoe UI', sans-serif;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #142B49;
}

section[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

/* Main headings */
h1 {
    color: #142B49 !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #1D3557 !important;
    font-weight: 650 !important;
}

/* Paragraphs */
p {
    color: #526176;
}

/* Cards and containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF;
    border: 1px solid #E3EAF2;
    border-radius: 12px;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E3EAF2;
    box-shadow: 0 2px 8px rgba(20,43,73,0.04);
}

div[data-testid="stMetricLabel"] {
    color: #64748B;
}

div[data-testid="stMetricValue"] {
    color: #142B49;
    font-weight: 700;
}

/* Primary buttons */
.stButton > button {
    background-color: #16A6A0;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 12px 20px;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #118780;
    color: #FFFFFF;
    border: none;
}

/* Download buttons */
.stDownloadButton > button {
    background-color: #142B49;
    color: white;
    border-radius: 8px;
    border: none;
}

/* Text areas */
textarea {
    border-radius: 8px !important;
}

/* File uploader */
div[data-testid="stFileUploader"] {
    background-color: #FFFFFF;
    border: 1px dashed #16A6A0;
    border-radius: 12px;
    padding: 15px;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid #E3EAF2;
    border-radius: 10px;
}

/* Expanders */
div[data-testid="stExpander"] {
    background-color: #FFFFFF;
    border: 1px solid #E3EAF2;
    border-radius: 10px;
}

/* Progress bar */
div[data-testid="stProgressBar"] > div > div {
    background-color: #16A6A0;
}

/* Divider */
hr {
    border-color: #E3EAF2;
}

/* Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)



# =====================================================
# 3. GEMINI API CONFIGURATION
# =====================================================

@st.cache_resource
def initialize_gemini():

    api_key = st.secrets["GEMINI_API_KEY"]

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=api_key,
        temperature=0.2
    )

    return llm


# =====================================================
# 4. RESUME TEXT EXTRACTION
# =====================================================

def extract_pdf_text(file):

    pdf_reader = PdfReader(file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    for table in document.tables:
        for row in table.rows:
            text += " | ".join(
                cell.text for cell in row.cells
            ) + "\n"

    return text


def extract_resume_text(file):

    if file.name.lower().endswith(".pdf"):
        return extract_pdf_text(file)

    elif file.name.lower().endswith(".docx"):
        return extract_docx_text(file)

    else:
        raise ValueError("Unsupported file format")


# =====================================================
# 5. AI RESUME ANALYSIS PROMPT
# =====================================================


def analyze_resume(llm, resume_text, job_description):

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an experienced HR recruitment analyst
            and technical resume evaluator.

            Analyse the candidate resume against the
            provided job description.

            Evaluate the candidate fairly using only
            information available in the resume.

            Do not invent candidate information.

            Do not penalize candidates based on age,
            gender, religion, caste, race, disability,
            marital status or other protected characteristics.

            Evaluate professional qualifications,
            relevant skills and experience only.

            Return ONLY valid JSON without markdown fences.

            Use this exact JSON structure:

            {{
                "candidate_name": "Candidate name",
                "email": "Email address or Not Provided",
                "phone": "Phone number or Not Provided",
                "location": "Location or Not Provided",
                "qualification": "Educational qualification",
                "total_experience": "Experience or Fresher",
                "previous_companies": [],
                "technical_skills": [],
                "matched_skills": [],
                "missing_skills": [],
                "match_percentage": 0,
                "experience_match": "Explanation",
                "qualification_match": "Explanation",
                "strengths": [],
                "weaknesses": [],
                "recommendations": [],
                "interview_questions": [
                    {{
                        "question": "Question",
                        "answer": "Suggested answer"
                    }}
                ],
                "overall_assessment": "Detailed assessment",
                "shortlisting_recommendation": "Review"
            }}

            Match percentage must be an integer between
            0 and 100.

            Base the score on relevant skills,
            qualifications, experience and job requirements.

            Do not automatically treat missing information
            as proof that the candidate lacks a skill.

            Shortlisting recommendation should be one of:
            Strong Match, Potential Match, Low Match,
            or Manual Review.

            Generate only 3 relevant technical interview questions
            with short suggested answers.

            Keep the overall assessment within 100 words.

            Keep strengths, weaknesses and recommendations
            to a maximum of 3 points each.

            Return concise JSON without unnecessary explanations.    
            """
        ),
        (
            "human",
            """
            JOB DESCRIPTION:

            {job_description}

            RESUME CONTENT:

            {resume_text}
            """
        )
    ])

    chain = prompt | llm

    response = chain.invoke({
        "job_description": job_description,
        "resume_text": resume_text
    })

    return response.content



# =====================================================
# 6. JSON RESPONSE PROCESSING
# =====================================================

def parse_ai_response(response):

    if isinstance(response, list):
        response = "".join(
            item.get("text", "") if isinstance(item, dict)
            else str(item)
            for item in response
        )

    response = str(response).strip()

    response = re.sub(
        r"^```(?:json)?\s*",
        "",
        response,
        flags=re.IGNORECASE
    )

    response = re.sub(
        r"\s*```$",
        "",
        response
    )

    start = response.find("{")
    end = response.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("AI did not return valid JSON.")

    return json.loads(response[start:end + 1])


# =====================================================
# 7. DOWNLOAD REPORT
# =====================================================

def create_report(candidate):

    report = f"""
RESUME - JOB DESCRIPTION MATCH REPORT

Candidate Name: {candidate.get('candidate_name')}
Email: {candidate.get('email')}
Phone: {candidate.get('phone')}
Location: {candidate.get('location')}

Qualification:
{candidate.get('qualification')}

Experience:
{candidate.get('total_experience')}

Match Percentage:
{candidate.get('match_percentage')}%

Matched Skills:
{', '.join(candidate.get('matched_skills', []))}

Missing Skills:
{', '.join(candidate.get('missing_skills', []))}

Technical Skills:
{', '.join(candidate.get('technical_skills', []))}

Experience Match:
{candidate.get('experience_match')}

Qualification Match:
{candidate.get('qualification_match')}

Strengths:
{chr(10).join(candidate.get('strengths', []))}

Weaknesses:
{chr(10).join(candidate.get('weaknesses', []))}

Recommendations:
{chr(10).join(candidate.get('recommendations', []))}

Overall Assessment:
{candidate.get('overall_assessment')}

Shortlisting Recommendation:
{candidate.get('shortlisting_recommendation')}
"""

    for index, item in enumerate(
        candidate.get("interview_questions", []), 1
    ):
        report += (
            f"\n\nInterview Question {index}:\n"
            f"{item.get('question', '')}\n"
            f"Suggested Answer:\n{item.get('answer', '')}"
        )

    return report


# =====================================================
# 8. DISPLAY CANDIDATE RESULTS
# =====================================================

def display_candidate_result(candidate):

    name = candidate.get("candidate_name", "Candidate")

    st.markdown("---")

    st.header(f"👤 {name}")

    # KPI Cards

    col1, col2, col3 = st.columns(3)

    score = candidate.get("match_percentage", 0)

    col1.metric(
        "Resume Match",
        f"{score}%"
    )

    col2.metric(
        "Matched Skills",
        len(candidate.get("matched_skills", []))
    )

    col3.metric(
        "Missing Skills",
        len(candidate.get("missing_skills", []))
    )

    st.progress(
        max(0, min(100, score)) / 100
    )

    # Candidate information

    st.subheader("📋 Candidate Information")

    info1, info2 = st.columns(2)

    with info1:
        st.write("**Email:**", candidate.get("email"))
        st.write("**Phone:**", candidate.get("phone"))
        st.write("**Location:**", candidate.get("location"))

    with info2:
        st.write("**Qualification:**", candidate.get("qualification"))
        st.write("**Experience:**", candidate.get("total_experience"))

    st.write(
        "**Previous Companies:**",
        ", ".join(candidate.get("previous_companies", []))
    )

    # Skills analysis

    st.subheader("💡 Skills Analysis")

    skill1, skill2 = st.columns(2)

    with skill1:
        st.markdown("**✅ Matching Skills**")

        for skill in candidate.get("matched_skills", []):
            st.write(f"✓ {skill}")

    with skill2:
        st.markdown("**⚠️ Missing Skills**")

        for skill in candidate.get("missing_skills", []):
            st.write(f"• {skill}")

    st.markdown("**All Technical Skills**")

    st.write(
        ", ".join(candidate.get("technical_skills", []))
    )

    # Experience and qualification

    st.subheader("🎓 Experience & Qualification")

    st.write(
        "**Experience Match:**",
        candidate.get("experience_match")
    )

    st.write(
        "**Qualification Match:**",
        candidate.get("qualification_match")
    )

    # Strengths and weaknesses

    st.subheader("📊 Candidate Evaluation")

    evaluation1, evaluation2 = st.columns(2)

    with evaluation1:
        st.markdown("**Strengths**")

        for item in candidate.get("strengths", []):
            st.success(item)

    with evaluation2:
        st.markdown("**Areas to Improve**")

        for item in candidate.get("weaknesses", []):
            st.warning(item)

    # Recommendations

    st.subheader("🚀 Improvement Recommendations")

    for item in candidate.get("recommendations", []):
        st.write(f"• {item}")

    # Interview questions

    st.subheader("🎯 Interview Questions")

    questions = candidate.get("interview_questions", [])

    for index, item in enumerate(questions, 1):

        with st.expander(f"Question {index}: {item.get('question', '')}"):

            st.write("**Suggested Answer:**")

            st.write(item.get("answer", ""))

    # Overall assessment

    st.subheader("📝 Overall Assessment")

    st.write(candidate.get("overall_assessment"))

    st.subheader("Recruitment Recommendation")

    st.info(
        candidate.get(
            "shortlisting_recommendation",
            "Manual Review"
        )
    )

    # Download report

    report = create_report(candidate)

    st.download_button(
        label="⬇️ Download Candidate Report",
        data=report,
        file_name=f"{name.replace(' ', '_')}_report.txt",
        mime="text/plain"
    )


# =====================================================
# 9. MAIN APPLICATION HEADER
# =====================================================

st.title("📄 AI Resume - Job Description Matcher")

st.markdown(
    """
    <p class="subtitle">
    Intelligent Resume Screening and Candidate Evaluation
    using LangChain and Google Gemini.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# =====================================================
# 10. SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <h2 style="color:white;">
        ◈ TalentMatch AI
    </h2>
    <p style="color:#B9C9DA;">
        Recruitment Intelligence Platform
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### Navigation")

    st.markdown("📊 Candidate Dashboard")
    st.markdown("📄 Resume Screening")
    st.markdown("📋 Job Description")
    st.markdown("📈 Candidate Reports")

    st.divider()

    st.markdown("### Supported Documents")
    st.markdown("📄 PDF Documents")
    st.markdown("📝 Word Documents")

    st.divider()

    st.caption(
        "AI-assisted recruitment. "
        "All hiring decisions require human review."
    )


# =====================================================
# 11. JOB DESCRIPTION INPUT
# =====================================================

st.subheader("1. Enter Job Description")

job_description = st.text_area(
    "Paste the complete job description here",
    height=250,
    placeholder="""
    Example:

    Job Title: Junior Data Analyst

    Required Skills:
    Python, SQL, Excel, Power BI

    Qualification:
    BE / BTech / BSc

    Experience:
    0-1 years
    """
)


# =====================================================
# 12. RESUME UPLOAD
# =====================================================

st.subheader("2. Upload Candidate Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF or DOCX resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} resume(s) uploaded successfully!"
    )

    for file in uploaded_files:
        st.write(f"📄 {file.name}")


# =====================================================
# 13. ANALYSE BUTTON
# =====================================================

if st.button(
    "🚀 Analyse Resumes",
    type="primary",
    use_container_width=True
):

    if not job_description.strip():

        st.error("Please enter a job description.")

    elif not uploaded_files:

        st.error("Please upload at least one resume.")

    else:

        try:

            llm = initialize_gemini()

            results = []

            st.subheader("3. Resume Analysis Results")

            progress = st.progress(0)

            status = st.empty()

            for index, file in enumerate(uploaded_files):

                status.info(
                    f"Analysing {file.name}..."
                )

                try:

                    resume_text = extract_resume_text(file)

                    if not resume_text.strip():
                        raise ValueError(
                            "No readable text found. "
                            "This may be a scanned PDF."
                        )

                    if len(resume_text) > 12000:
                       resume_text = resume_text[:12000]

                    start_time = time.time()

                    ai_response = analyze_resume(
                    llm,
                    resume_text,
                    job_description
                    )

                    end_time = time.time()

                    analysis_time = end_time - start_time

                    st.success(
                     f"Gemini analysis completed in {analysis_time:.2f} seconds"
                    )

                    candidate = parse_ai_response(
                        ai_response
                    )

                    candidate["file_name"] = file.name

                    results.append(candidate)

                except Exception as e:

                    st.error(
                        f"Error analysing {file.name}: {e}"
                    )

                progress.progress(
                    (index + 1) / len(uploaded_files)
                )

            status.success("Resume analysis completed!")

            # Save results in session state

            st.session_state["results"] = results

        except Exception as e:

            st.error(f"Application error: {e}")


# =====================================================
# 14. DISPLAY ANALYSIS RESULTS
# =====================================================

if st.session_state.get("results"):

    results = st.session_state["results"]

    st.divider()

    st.header("📊 Candidate Comparison Dashboard")

    comparison_data = []

    for candidate in results:

        comparison_data.append({

            "Candidate Name":
                candidate.get("candidate_name"),

            "File Name":
                candidate.get("file_name"),

            "Match Score (%)":
                candidate.get("match_percentage"),

            "Qualification":
                candidate.get("qualification"),

            "Experience":
                candidate.get("total_experience"),

            "Recommendation":
                candidate.get("shortlisting_recommendation")

        })

    df = pd.DataFrame(comparison_data)

    if not df.empty:

        df = df.sort_values(
            by="Match Score (%)",
            ascending=False
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        # CSV download

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "⬇️ Download Candidate Comparison CSV",
            data=csv_data,
            file_name="candidate_comparison.csv",
            mime="text/csv"
        )

    # Individual candidate reports

    st.header("📑 Individual Candidate Reports")

    for candidate in results:

        with st.expander(
            f"View {candidate.get('candidate_name', 'Candidate')} Report"
        ):

            display_candidate_result(candidate)


# =====================================================
# 15. FOOTER
# =====================================================

st.divider()

st.caption(
    "AI Resume Matcher | Built with Streamlit, "
    "LangChain and Google Gemini"
)
