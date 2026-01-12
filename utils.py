import re
import pandas as pd
from datetime import datetime
import PyPDF2
import docx

SKILL_PHRASES = [
    "java", "python",
    "spring boot",
     "microservices",
    "CI/Cd","DBMS","R","C","C++",
     "C#","sql", "mysql",
    "docker", "kubernetes"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s/]', '', text)
    return text

def extract_skills(text):
    text = clean_text(text)
    return {skill for skill in SKILL_PHRASES if skill in text}

def skill_match(resume, jd):
    r = extract_skills(resume)
    j = extract_skills(jd)
    matched = r & j
    missing = j - r
    if j :         # It check whether j has skills
        percent = round((len(matched)/len(j))*100,2)
    else :
        percent = 0 # if j has  no skills it cause an error because 0 is not divide any number
    return matched, missing, percent

def extract_experience(text):
    match = re.search(r'(\d+(?:\.\d+)?)\s*(year|years|y)', text.lower())
    return float(match.group(1)) if match else None

def experience_match(resume, jd):
    return extract_experience(resume), extract_experience(jd)

def final_score(skill_percent, resume_exp, jd_exp):
    score = 0.75 * skill_percent
    if resume_exp and jd_exp:
        score += min((resume_exp / jd_exp) * 25, 25)
    return round(score, 2)

def save_to_dataset(skill_percent, final_score):
    row = {
        "skill_percentage": skill_percent,
        "final_score": final_score,
        "time": datetime.now()
    }
    df = pd.DataFrame([row])
    try:
        old = pd.read_csv("dataset.csv")
        df = pd.concat([old, df], ignore_index=True)
    except:
        pass
    df.to_csv("dataset.csv", index=False)

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join([p.extract_text() or "" for p in reader.pages])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return " ".join(p.text for p in doc.paragraphs)
