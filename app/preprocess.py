import re
import string

stop_words = {
    "the","and","is","in","of","to","a","for","on","with","as","by","an","be",
    "this","that","it","from","at","or","are","was","were"
}

def clean_and_tokenize(text: str):
    """Simple tokenizer: lowercase, remove punctuation, split, remove stopwords."""
    
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    
    tokens = [t for t in tokens if t not in stop_words and t.isalpha()]
    
    return tokens

def extract_nouns(tokens):
    """Simple noun guess: words ending not with -ing/-ed etc."""
    nouns = []
    for t in tokens:
        if not t.endswith(("ing", "ed")):
            nouns.append(t)
    return nouns
