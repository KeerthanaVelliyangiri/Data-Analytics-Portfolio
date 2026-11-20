# ResumeSync — AI Career & Recruitment Platform

A modular Streamlit prototype with Recruiter Mode and Job Seeker Mode. It supports PDF/DOCX extraction, heuristic resume validation, Gemini-first/Groq-fallback LLM calls, candidate comparison, evidence-grounded recruiter Q&A using FAISS, job-seeker skill-gap guidance, a career roadmap and mock interview practice.

## 1. Requirements
- Python 3.10–3.12 recommended
- A Gemini API key, Groq API key, or both
- Internet access for model APIs and first-time Hugging Face embedding-model download

## 2. Install
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Configure API keys
Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and replace the example values. Never commit the real secrets file. Environment variables `GEMINI_API_KEY` and `GROQ_API_KEY` are also supported.

The application prefers Gemini and falls back to Groq if the Gemini request fails. To use Groq only, omit the Gemini key.

## 4. Run
```bash
streamlit run app.py
```

## 5. Modes
- **Recruiter Mode:** paste one job description, upload multiple resumes, screen valid documents, filter candidates and ask evidence-based questions.
- **Job Seeker Mode:** upload one resume, compare it with a target role, request a skill-gap plan, career roadmap and mock interview questions.

## 6. Important limitations
- Resume validation is a heuristic pre-check, not a perfect classifier. Review rejected/accepted files.
- Scanned PDFs need OCR; this version reports when no usable text can be extracted and does not silently analyse blank text.
- Job-search items are search links, not a verified live vacancy feed. A production integration should use permitted job APIs/feeds or official career pages and show checked dates.
- FAISS embeddings are generated locally using a Hugging Face sentence-transformer. The first use downloads the model. Recruiter Q&A searches the resumes currently uploaded in the active Streamlit session; it does not automatically search old saved reports.
- Workspace ID is a lightweight logical separation mechanism, not authentication. Do not deploy this prototype for multiple real customers without login, authorization, encryption, tenant-scoped storage and retention controls.
- AI match scores are estimates and must not be used as the sole basis for hiring decisions.

## 7. Suggested production improvements
Add authentication and role-based access, robust tenant isolation, OCR, audit logging, secure file storage, data deletion controls, rate limiting, evaluation tests and authorized job-board integrations before public multi-user deployment.
