
import streamlit as st
import pandas as pd
import json
import re
import time

from pypdf import PdfReader
from docx import Document

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="TalentMatch AI",
    page_icon="📄",
    layout="wide"
)


# =====================================================
# 2. CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #F4F7FB;
    color: #243247;
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

section[data-testid="stSidebar"] {
    background-color: #142B49;
}

section[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

h1 {
    color: #142B49 !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #1D3557 !important;
    font-weight: 650 !important;
}

p {
    color: #526176;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF;
    border: 1px solid #E3EAF2;
    border-radius: 12px;
}

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

.stDownloadButton > button {
    background-color: #142B49;
    color: white;
    border-radius: 8px;
    border: none;
}

textarea {
    border-radius: 8px !important;
}

div[data-testid="stFileUploader"] {
    background-color: #FFFFFF;
    border: 1px dashed #16A6A0;
    border-radius: 12px;
    padding: 15px;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #E3EAF2;
    border-radius: 10px;
}

div[data-testid="stExpander"] {
    background-color: #FFFFFF;
    border: 1px solid #E3EAF2;
    border-radius: 10px;
}

div[data-testid="stProgressBar"] > div > div {
    background-color: #16A6A0;
}

hr {
    border-color: #E3EAF2;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. AI API CONFIGURATION
# =====================================================

@st.cache_resource
def initialize_gemini():

    api_key = st.secrets.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Gemini API key is missing from Streamlit Secrets."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=0.2
    )

    return llm


@st.cache_resource
def initialize_groq():

    api_key = st.secrets.get("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "Groq API key is missing from Streamlit Secrets."
        )

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        api_key=api_key,
        temperature=0.2,
        max_retries=1,
        timeout=60
    )

    return llm


# =====================================================
# 4. RESUME TEXT EXTRACTION
# =====================================================

def extract_pdf_text(file):

    file.seek(0)

    pdf_reader = PdfReader(file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(file):

    file.seek(0)

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

        raise ValueError("Unsupported file format.")


# =====================================================
# 5. AI RESPONSE JSON PROCESSING
# =====================================================

def parse_ai_response(response):

    if isinstance(response, list):

        response = "".join(
            item.get("text", "")
            if isinstance(item, dict)
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

        raise ValueError(
            "AI did not return a valid JSON response."
        )

    result = json.loads(response[start:end + 1])

    if not isinstance(result, dict):

        raise ValueError(
            "AI response must be a JSON object."
        )

    return result


# =====================================================
# 6. AI RESUME ANALYSIS PROMPT
# =====================================================


def analyze_resume(resume_text, job_description):

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an experienced HR recruitment analyst
            and technical resume evaluator.

            Analyse the candidate resume against the
            provided job description.

            Evaluate fairly using only information
            available in the resume.

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

            Generate only 3 relevant technical interview
            questions with short suggested answers.

            Keep the overall assessment within 100 words.

            Keep strengths, weaknesses and recommendations
            to a maximum of 3 points each.

            Return concise JSON.
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

    # Try Gemini first, then Groq

    providers = [
        ("Gemini", initialize_gemini),
        ("Groq", initialize_groq)
    ]

    errors = []

    for provider_name, initialize_model in providers:

        try:

            llm = initialize_model()

            chain = prompt | llm

            response = chain.invoke({
                "job_description": job_description,
                "resume_text": resume_text
            })

            candidate = parse_ai_response(
                response.content
            )

            return candidate, provider_name

        except Exception as e:

            errors.append(
                f"{provider_name}: {str(e)[:300]}"
            )

            continue

    raise RuntimeError(
        "Both AI providers failed:\n"
        + "\n".join(errors)
    )


# =====================================================
# 7. DOWNLOAD REPORT
# =====================================================

def create_report(candidate):

    report = f"""
TALENTMATCH AI
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
            f"Suggested Answer:\n"
            f"{item.get('answer', '')}"
        )

    return report


# =====================================================
# 8. DISPLAY CANDIDATE RESULTS
# =====================================================

def display_candidate_result(candidate):

    name = candidate.get(
        "candidate_name",
        "Candidate"
    )

    st.markdown("---")

    st.header(f"👤 {name}")

    # KPI Cards

    col1, col2, col3 = st.columns(3)

    score = candidate.get(
        "match_percentage", 0
    )

    try:

        score = int(score)

    except (ValueError, TypeError):

        score = 0

    score = max(0, min(100, score))

    matched = candidate.get("matched_skills", [])
    missing = candidate.get("missing_skills", [])

    col1.metric(
        "Resume Match",
        f"{score}%"
    )

    col2.metric(
        "Matched Skills",
        len(matched)
    )

    col3.metric(
        "Missing Skills",
        len(missing)
    )

    st.progress(score / 100)

    # Candidate information

    st.subheader("📋 Candidate Information")

    info1, info2 = st.columns(2)

    with info1:

        st.write(
            "**Email:**",
            candidate.get("email")
        )

        st.write(
            "**Phone:**",
            candidate.get("phone")
        )

        st.write(
            "**Location:**",
            candidate.get("location")
        )

    with info2:

        st.write(
            "**Qualification:**",
            candidate.get("qualification")
        )

        st.write(
            "**Experience:**",
            candidate.get("total_experience")
        )

    st.write(
        "**Previous Companies:**",
        ", ".join(candidate.get("previous_companies", []))
    )

    # Skills analysis

    st.subheader("💡 Skills Analysis")

    skill1, skill2 = st.columns(2)

    with skill1:

        st.markdown("**✅ Matching Skills**")

        for skill in matched:
            st.write(f"✓ {skill}")

    with skill2:

        st.markdown("**⚠️ Missing Skills**")

        for skill in missing:
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

    questions = candidate.get(
        "interview_questions", []
    )

    for index, item in enumerate(questions, 1):

        with st.expander(
            f"Question {index}: {item.get('question', '')}"
        ):

            st.write("**Suggested Answer:**")

            st.write(item.get("answer", ""))

    # Overall assessment

    st.subheader("📝 Overall Assessment")

    st.write(
        candidate.get("overall_assessment")
    )

    st.subheader("Recruitment Recommendation")

    st.info(
        candidate.get(
            "shortlisting_recommendation",
            "Manual Review"
        )
    )

    # Download report

    report = create_report(candidate)

    safe_name = re.sub(
        r"[^A-Za-z0-9_-]",
        "_",
        str(name)
    )

    st.download_button(
        label="⬇️ Download Candidate Report",
        data=report,
        file_name=f"{safe_name}_report.txt",
        mime="text/plain",
        key=f"report_{safe_name}_{candidate.get('file_name', '')}"
    )


# =====================================================
# 9. SESSION STATE
# =====================================================

if "results" not in st.session_state:

    st.session_state["results"] = []


# =====================================================
# 10. MAIN APPLICATION HEADER
# =====================================================

st.title("TalentMatch AI")

st.markdown(
    """
    <p class="subtitle">
    Recruitment Intelligence Platform
    <br>
    Intelligent Resume Screening and Candidate Evaluation
    using LangChain, Google Gemini and Groq.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# =====================================================
# 11. SIDEBAR
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
# 12. JOB DESCRIPTION INPUT
# =====================================================

st.subheader("Enter Job Description")

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
# 14. RESUME UPLOAD
# =====================================================

st.subheader("Upload Candidate Resumes")

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
# 15. ANALYSE BUTTON
# =====================================================

if st.button(
    " Analyse Resumes",
    type="primary",
    use_container_width=True
):

    if not job_description.strip():

        st.error(
            "Please enter a job description."
        )

    elif not uploaded_files:

        st.error(
            "Please upload at least one resume."
        )

    else:

        # Clear old results before a new analysis

        st.session_state["results"] = []

        results = []

        st.subheader("4. Resume Analysis Results")

        progress = st.progress(0)

        status = st.empty()

        for index, file in enumerate(uploaded_files):

            status.info(
                f"Analysing {file.name}..."
            )

            try:

                # Extract resume text

                resume_text = extract_resume_text(file)

                if not resume_text.strip():

                    raise ValueError(
                        "No readable text found. "
                        "This may be a scanned PDF."
                    )

                # Limit resume content

                if len(resume_text) > 12000:

                    resume_text = resume_text[:12000]

                # Start timer

                start_time = time.time()

                # AI analysis with provider selection

                candidate, provider_used = analyze_resume(
                    resume_text,
                    job_description,
                    
                )

                # End timer

                end_time = time.time()

                analysis_time = end_time - start_time

                # Save candidate details

                candidate["file_name"] = file.name

                candidate["ai_provider"] = provider_used

                results.append(candidate)

                st.success(
                    f"{provider_used} analysis completed "
                    f"in {analysis_time:.2f} seconds "
                    f"for {file.name}"
                )

            except Exception as e:

                st.error(
                    f"Error analysing {file.name}: {str(e)}"
                )

            # Update progress

            progress.progress(
                (index + 1) / len(uploaded_files)
            )

        # Save successful results

        st.session_state["results"] = results

        if results:

            status.success(
                f"Successfully analysed {len(results)} "
                f"out of {len(uploaded_files)} resume(s)!"
            )

        else:

            status.error(
                "No resumes could be analysed. "
                "Please check your API keys, model availability "
                "and API quotas."
            )


# =====================================================
# 16. CANDIDATE COMPARISON DASHBOARD
# =====================================================

if st.session_state["results"]:

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

        df["Match Score (%)"] = pd.to_numeric(
            df["Match Score (%)"],
            errors="coerce"
        )

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

    for index, candidate in enumerate(results):

        with st.expander(
            f"View {candidate.get('candidate_name', 'Candidate')} Report"
        ):

            display_candidate_result(candidate)


# =====================================================
# 17. FOOTER
# =====================================================

st.divider()

st.caption(
    "TalentMatch AI | Built with Streamlit, LangChain, "
    "Google Gemini and Groq."
)

st.caption(
    "AI-generated assessments are decision-support tools "
    "and must be reviewed by human recruiters."
)
