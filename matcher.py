import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SKILLS = [
    "python",
    "java",
    "javascript",
    "c++",
    "sql",
    "mysql",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "generative ai",
    "large language models",
    "llm",
    "rag",
    "langchain",
    "tensorflow",
    "pytorch",
    "flask",
    "django",
    "html",
    "css",
    "rest api",
    "api integration",
    "data analysis",
    "data visualization",
    "statistics",
    "feature engineering",
    "model evaluation",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "excel",
    "power bi",
    "tableau",
]


def find_skills(text):
    """Find recognized skills mentioned in a block of text."""

    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(found_skills)


def analyze_resume(resume_text, job_description):
    """Compare resume text with a job description."""

    if not resume_text or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    # Calculate text similarity using TF-IDF.
    documents = [
        resume_text.lower(),
        job_description.lower()
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    try:
        vectors = vectorizer.fit_transform(documents)
    except ValueError as error:
        raise ValueError(
            "Not enough meaningful text to compare. "
            "Please provide a longer resume and job description."
        ) from error

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    # Identify skills in each document.
    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description)

    matched_skills = sorted(
        set(resume_skills) & set(job_skills)
    )

    missing_skills = sorted(
        set(job_skills) - set(resume_skills)
    )

    return {
        "similarity_score": round(float(similarity) * 100, 2),
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }