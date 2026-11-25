# ResumeSync – AI Career & Recruitment Platform

ResumeSync is an AI-powered career and recruitment web application I developed using Python, Streamlit, and AI technologies. The main idea behind this project is to help recruiters screen candidate resumes against job descriptions and help job seekers understand their skills, identify skill gaps, and improve their career opportunities in one place.

## Features

- **Recruiter Mode:** Recruiters can upload multiple PDF and DOCX resumes and screen candidates against a job description.
- **Candidate Comparison:** Compares candidates based on matched skills, missing skills, qualifications, experience, and estimated match percentage.
- **Candidate Filtering:** Allows recruiters to filter candidates based on available candidate details and match score.
- **Recruiter AI Assistant:** Recruiters can ask questions about screened candidates and get AI-generated responses.
- **Job Seeker Mode:** Job seekers can upload their resumes and analyze them against a target job description.
- **Resume Analysis:** Identifies matched skills, missing skills, strengths, improvement areas, and estimated job match percentage.
- **Skill Gap Analysis:** Generates recommendations to improve missing skills based on job requirements.
- **Career Roadmap:** Creates an AI-powered eight-week career development plan.
- **Job Search Assistance:** Generates job search links based on the user's target job role and preferred location.
- **Mock Interview Practice:** Generates interview questions and evaluates user answers with AI feedback.
- **CSV Export:** Allows recruiters to download candidate comparison results.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Groq API
- LangChain
- HuggingFace Embeddings
- FAISS
- SQLite
- Pandas
- PyPDF
- Python-docx

## How It Works

ResumeSync provides two separate modes: Recruiter Mode and Job Seeker Mode.

In Recruiter Mode, recruiters upload multiple resumes and provide a job description. The application extracts resume content, validates documents, and uses AI to analyze candidates. It identifies matching and missing skills, generates estimated match percentages, and displays candidate comparison results.

In Job Seeker Mode, users upload their resumes and enter a target job description. The AI analyzes the resume and provides an estimated match percentage, matched skills, missing skills, strengths, and improvement areas. Users can also generate skill-gap recommendations, career roadmaps, job search links, and practice mock interviews.

The AI integration uses Google Gemini as the primary provider and Groq as an automatic fallback provider. LangChain manages LLM interactions, while HuggingFace embeddings and FAISS support vector-based document retrieval. SQLite is used to store application reports.

<img width="1112" height="569" alt="screenshottwo" src="https://github.com/user-attachments/assets/a75ffdbf-1860-417b-a39e-3b182642544a" />
<img width="1117" height="569" alt="screenshotone" src="https://github.com/user-attachments/assets/cb77f32e-7d3f-4ade-8a12-fdf8993d3320" />

## Run the Project Locally

1. Clone the repository

    ```bash
    git clone https://github.com/KeerthanaVelliyangiri/Data-Analytics-Portfolio.git
    ```

2. Open the project folder

    ```bash
    cd Data-Analytics-Portfolio/ResumeSync
    ```

3. Create and activate a virtual environment

    ```bash
    python -m venv venv
    ```

    Windows:

    ```bash
    venv\Scripts\activate
    ```

4. Install the required packages

    ```bash
    pip install -r requirements.txt
    ```

5. Configure your Gemini and Groq API credentials

    Create `.streamlit/secrets.toml` and add your API credentials using the secret names expected by the application. Never upload this file to GitHub.

6. Start the application

    ```bash
    streamlit run app.py
    ```

## Live Application

https://resumematchkeerthi.streamlit.app/

## Project Testing

The application was deployed using Streamlit Community Cloud. Both Recruiter Mode and Job Seeker Mode are available in the deployed application.

The main workflows include resume uploading, document validation, AI resume analysis, candidate comparison, skill-gap recommendations, career roadmap generation, and mock interview practice.

## Future Improvements

- Add secure user login and registration.
- Implement role-based access and improved user data isolation.
- Add advanced recruitment analytics and dashboards.
- Improve resume parsing and skill extraction.
- Add personalized job recommendations.
- Improve RAG-based question answering with source evidence.
- Add career progress tracking for job seekers.

## Developer

Keerthana Velliyangiri

B.E. – Computer Science and Engineering

- GitHub: https://github.com/KeerthanaVelliyangiri
- Project Repository: https://github.com/KeerthanaVelliyangiri/Data-Analytics-Portfolio/tree/main/ResumeSync
- Live Application: https://resumematchkeerthi.streamlit.app/
