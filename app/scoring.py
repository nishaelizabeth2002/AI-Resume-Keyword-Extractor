from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.keywords import extract_keywords, SKILL_KEYWORDS

def compute_similarity(resume_text: str, job_text: str):
    """Return cosine similarity between resume and job description."""

    vectorizer = TfidfVectorizer(stop_words='english')

    vectors = vectorizer.fit_transform([resume_text, job_text])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return similarity


def compute_skill_match(resume_text: str, job_text: str):
    """Compare skills in resume vs important skills in job posting."""

    resume_kw = extract_keywords(resume_text)
    job_kw = extract_keywords(job_text)

    resume_skills = set(resume_kw["skills_found"])
    job_skills = set(job_kw["skills_found"])

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    return matched, missing


def calculate_match_score(resume_text: str, job_text: str):
    """Returns a score from 0–100 based on similarity + skill match."""

    base_similarity = compute_similarity(resume_text, job_text)

    matched, missing = compute_skill_match(resume_text, job_text)

    # Convert similarity (0–1) to a 0–70 scale
    similarity_score = base_similarity * 70

    # Skill bonus (up to 30 points)
    skill_score = (len(matched) / max(1, len(matched) + len(missing))) * 30

    final_score = similarity_score + skill_score

    return {
        "final_score": round(final_score, 2),
        "similarity": round(base_similarity, 3),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }
