# AI Resume Screening & Ranking System (ATS)

This project simulates an Applicant Tracking System (ATS) that analyzes and ranks resumes against a job description using Natural Language Processing (NLP).

## Features
- Upload multiple resume PDFs
- Extract skills automatically
- Semantic matching using TF-IDF
- Final ATS score using weighted scoring
- Candidate ranking & shortlisting
- Resume improvement suggestions

## Tech Stack
- Python
- NLP (TF-IDF, Cosine Similarity)
- Streamlit
- Scikit-learn
- PyPDF2

## How It Works
1. Resume PDFs are converted into text
2. Text is cleaned and normalized
3. Skills are extracted using regex
4. Resume and job description are compared
5. Final ATS score is calculated
6. Candidates are ranked automatically

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
