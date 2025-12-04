from app.preprocess import clean_and_tokenize, extract_nouns

# A simple skill list (you can expand it later)
SKILL_KEYWORDS = {
    "python", "java", "c++", "javascript", "react", "node",
    "aws", "azure", "gcp", "docker", "kubernetes",
    "sql", "mysql", "postgresql", "mongodb",
    "machine learning", "deep learning", "nlp",
    "tensorflow", "pytorch", "scikit-learn",
    "fastapi", "flask", "django",
    "data analysis", "pandas", "numpy"
}

def extract_keywords(text: str):
    """
    Extract useful keywords from text.
    Uses preprocessing → noun extraction → skill matching.
    """
    tokens = clean_and_tokenize(text)
    nouns = extract_nouns(tokens)

    # Direct matched skills
    matched_skills = set()

    for word in tokens:
        if word in SKILL_KEYWORDS:
            matched_skills.add(word)
    
    for noun in nouns:
        if noun in SKILL_KEYWORDS:
            matched_skills.add(noun)

    return {
        "tokens": tokens,
        "nouns": nouns,
        "skills_found": list(matched_skills)
    }
