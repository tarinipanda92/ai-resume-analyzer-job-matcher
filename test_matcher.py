from matcher import analyze_resume


resume = """
Graduate Engineer with experience in Python, Pandas, NumPy,
Flask, SQL, data analysis and GitHub. Built machine learning
projects using Scikit-learn and evaluated model performance.
"""

job_description = """
We are looking for a Junior AI/ML Engineer with Python,
SQL, machine learning, Scikit-learn, Flask, Docker,
AWS and experience with model evaluation.
"""


result = analyze_resume(resume, job_description)

print("=" * 45)
print("AI RESUME ANALYZER - TEST REPORT")
print("=" * 45)

print("\nText similarity score:")
print(f"{result['similarity_score']}%")

print("\nSkills found in resume:")
print(", ".join(result["resume_skills"]) or "None found")

print("\nSkills mentioned in job description:")
print(", ".join(result["job_skills"]) or "None found")

print("\nMatched skills:")
print(", ".join(result["matched_skills"]) or "None found")

print("\nPotentially missing skills:")
print(", ".join(result["missing_skills"]) or "None found")

print("\nTest completed successfully!")