import os
from types import SimpleNamespace
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq


def _secret(name):
    try:
        return st.secrets.get(name, os.getenv(name, ""))
    except Exception:
        return os.getenv(name, "")


class GeminiGroqFallback:
    """LangChain-compatible invoke wrapper: Gemini first, Groq on request failure."""
    def __init__(self, gemini=None, groq=None):
        self.gemini = gemini
        self.groq = groq

    def invoke(self, prompt):
        last_error = None
        if self.gemini is not None:
            try:
                return self.gemini.invoke(prompt)
            except Exception as exc:
                last_error = exc
        if self.groq is not None:
            try:
                return self.groq.invoke(prompt)
            except Exception as exc:
                last_error = exc
        raise RuntimeError(f"No configured AI provider completed the request. Last error: {last_error}")


def get_llm():
    gemini = groq = None
    gemini_key, groq_key = _secret("GEMINI_API_KEY"), _secret("GROQ_API_KEY")
    if gemini_key:
        try:
            gemini = ChatGoogleGenerativeAI(model=_secret("GEMINI_MODEL") or "gemini-2.5-flash", google_api_key=gemini_key, temperature=0.1)
        except Exception:
            gemini = None
    if groq_key:
        try:
            groq = ChatGroq(model=_secret("GROQ_MODEL") or "openai/gpt-oss-20b", groq_api_key=groq_key, temperature=0.1)
        except Exception:
            groq = None
    if gemini is None and groq is None:
        return None
    return GeminiGroqFallback(gemini, groq)


def provider_status():
    if _secret("GEMINI_API_KEY") and _secret("GROQ_API_KEY"):
        return "Gemini primary · Groq automatic fallback"
    if _secret("GEMINI_API_KEY"):
        return "Gemini configured (no fallback key)"
    if _secret("GROQ_API_KEY"):
        return "Groq configured"
    return "No API key configured"
