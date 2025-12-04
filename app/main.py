from fastapi import FastAPI, UploadFile, File, Form
from app.parser import extract_text
from app.keywords import extract_keywords
from app.scoring import calculate_match_score

app = FastAPI(title="Resume Keyword Extractor + Job Match Scorer")

@app.get("/")
def root():
    return {"status": "running", "message": "API is working!"}

@app.post("/extract")
async def extract_from_text(text: str = Form(...)):
    result = extract_keywords(text)
    return result

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    extracted = extract_text(temp_path)
    return {"file": file.filename, "extracted_text": extracted}

@app.post("/match")
async def match_resume_and_job(
    file: UploadFile = File(...),
    job_text: str = Form(...)
):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    resume_text = extract_text(temp_path)
    score = calculate_match_score(resume_text, job_text)

    return {"resume": file.filename, "score": score}
