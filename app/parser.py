import pdfminer.high_level
import docx
import os

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from PDF using pdfminer."""
    try:
        text = pdfminer.high_level.extract_text(file_path)
        return text or ""
    except Exception as e:
        return f"PDF extraction error: {e}"

def extract_text_from_docx(file_path: str) -> str:
    """Extracts text from DOCX using python-docx."""
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"DOCX extraction error: {e}"

def extract_text(file_path: str) -> str:
    """Detect file type and extract text accordingly."""
    extension = file_path.lower().split(".")[-1]

    if extension == "pdf":
        return extract_text_from_pdf(file_path)
    elif extension == "docx":
        return extract_text_from_docx(file_path)
    elif extension == "txt":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except:
            with open(file_path, "r", encoding="latin-1") as f:
                return f.read()
    else:
        return "Unsupported file type."
