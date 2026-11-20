from io import BytesIO
from pypdf import PdfReader
from docx import Document


def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    try:
        data = uploaded_file.getvalue()
        if name.endswith(".pdf"):
            reader = PdfReader(BytesIO(data))
            if reader.is_encrypted:
                return "", "This PDF is password-protected. Please upload an unlocked PDF."
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
        elif name.endswith(".docx"):
            doc = Document(BytesIO(data))
            text = "\n".join(p.text for p in doc.paragraphs)
            for table in doc.tables:
                for row in table.rows:
                    text += "\n" + " | ".join(cell.text for cell in row.cells)
        else:
            return "", "Unsupported file type. Upload PDF or DOCX."
        return text.strip(), None
    except Exception as exc:
        return "", f"Could not read {uploaded_file.name}: {exc}"
