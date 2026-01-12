import streamlit as st
from ats_engine import extract_text_from_pdf, calculate_ats_score

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Resume Screening ATS", layout="wide")

st.title("📄 AI Resume Screening & Ranking System")

# ---------- JOB DESCRIPTION ----------
job_description = st.text_area(
    "🧾 Paste Job Description Here",
    height=200
)

# ---------- SKILL SET ----------
skill_set = [
    'python', 'java', 'c\\+\\+', 'javascript',
    'machine learning', 'deep learning', 'nlp',
    'data science', 'sql', 'mysql',
    'html', 'css', 'react',
    'tensorflow', 'keras', 'pytorch',
    'git', 'github', 'linux',
    'docker', 'aws'
]

# ---------- FILE UPLOAD ----------
uploaded_files = st.file_uploader(
    "📂 Upload Resume PDFs",
    type="pdf",
    accept_multiple_files=True
)

# ---------- ANALYZE BUTTON ----------
if st.button("🚀 Analyze Resumes"):
    if not uploaded_files or not job_description:
        st.warning("Please upload resumes and provide a job description.")
    else:
        results = []

        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            score = calculate_ats_score(
                resume_text,
                job_description,
                skill_set
            )
            score["candidate"] = file.name
            results.append(score)

        ranked = sorted(
            results,
            key=lambda x: x["final_score"],
            reverse=True
        )

        st.subheader("🏆 Ranked Candidates")

        for i, c in enumerate(ranked, start=1):
            with st.expander(f"Rank {i}: {c['candidate']} — {c['final_score']}%"):
                st.write(f"**Semantic Score:** {c['semantic_score']}%")
                st.write(f"**Skill Score:** {c['skill_score']}%")
                st.write("**Matched Skills:**", ", ".join(c['matched_skills']))
                st.write("**Missing Skills:**", ", ".join(c['missing_skills']))
