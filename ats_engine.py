import re
import PyPDF2
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(pdf_file):
    try:
        text = ""
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
        return text
    except Exception:
        return ""

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

def extract_skills(text, skill_list):
    found = set()
    for skill in skill_list:
        pattern = r'\b' + skill + r'\b'
        if re.search(pattern, text):
            found.add(skill)
    return found

def calculate_ats_score(resume_text, job_text, skill_set):
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_text)

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform([clean_resume, clean_job])

    semantic_score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0] * 100

    resume_skills = extract_skills(clean_resume, skill_set)
    job_skills = extract_skills(clean_job, skill_set)

    skill_score = (len(resume_skills & job_skills) / len(job_skills)) * 100 if job_skills else 0
    final_score = (0.7 * semantic_score) + (0.3 * skill_score)

    return {
        "semantic_score": round(semantic_score, 2),
        "skill_score": round(skill_score, 2),
        "final_score": round(final_score, 2),
        "matched_skills": list(resume_skills & job_skills),
        "missing_skills": list(job_skills - resume_skills)
    }
  

