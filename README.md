

\# AI Resume Analyzer \& Job Matcher



An AI-powered web application that analyzes a resume against a job description, calculates text similarity, and identifies matching and potentially missing skills.



\## Features



\- Upload resumes in PDF or DOCX format.

\- Extract resume text using PyMuPDF and python-docx.

\- Compare resumes with job descriptions using TF-IDF and cosine similarity.

\- Identify matching skills using a predefined skills vocabulary.

\- Highlight potentially missing skills mentioned in the job description.

\- Display results through a responsive Flask web interface.

\- Process uploaded resume files in memory without saving them to disk.



\## Technology Stack



\- \*\*Language:\*\* Python

\- \*\*Web Framework:\*\* Flask

\- \*\*Machine Learning:\*\* Scikit-learn

\- \*\*Text Analysis:\*\* TF-IDF and cosine similarity

\- \*\*PDF Processing:\*\* PyMuPDF

\- \*\*DOCX Processing:\*\* python-docx

\- \*\*Data Handling:\*\* Pandas

\- \*\*Frontend:\*\* HTML and CSS

\- \*\*Version Control:\*\* Git and GitHub



\## Project Structure



```text

AI-Resume-Analyzer-Job-Matcher/

├── app.py

├── analyzer.py

├── matcher.py

├── test\_analyzer.py

├── test\_matcher.py

├── requirements.txt

├── .gitignore

├── templates/

│   └── index.html

└── static/

&#x20;   └── style.css

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd AI-Resume-Analyzer-Job-Matcher

```



Replace `YOUR\_GITHUB\_REPOSITORY\_URL` with the actual repository URL.



\### 2. Create and activate a Conda environment



```bash

conda create -n resume-matcher-ai python=3.11 -y

conda activate resume-matcher-ai

```



\### 3. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 4. Start the application



```bash

python app.py

```



Open the following address in your browser:



http://127.0.0.1:5000



\## How to Use



1\. Open the application in your browser.

2\. Upload a resume in PDF or DOCX format.

3\. Paste the job description into the input field.

4\. Click \*\*Analyze Resume\*\*.

5\. Review the text similarity score, matched skills, detected resume skills, and potentially missing skills.



\## How It Works



\### Resume Text Extraction



The application extracts text from PDF and DOCX files.



\### Text Similarity



TF-IDF converts resume and job-description text into numerical vectors. Cosine similarity compares these vectors to calculate a text similarity score.



\### Skill Matching



A predefined vocabulary identifies known skills in the resume and job description. The application reports skills found in both texts and skills mentioned in the job description but not detected in the resume.



\## Limitations



\- The similarity score is not an official ATS score or a probability of getting hired.

\- Skill detection depends on a predefined vocabulary and may miss synonyms or alternative phrasing.

\- The current version does not use a large language model or understand every skill in its full context.

\- Scanned PDF documents containing only images may require OCR.

\- Results should be reviewed by the user before making career decisions.



\## Future Improvements



\- Expand the skills vocabulary and support synonyms.

\- Add stronger semantic matching using sentence embeddings.

\- Generate resume improvement suggestions based on job requirements.

\- Add downloadable analysis reports.

\- Add automated tests, input validation, and deployment monitoring.

\- Deploy the application online.



\## Disclaimer



This project is intended for educational and career-development purposes. Its similarity score and skill matches should not be interpreted as an official ATS evaluation or a hiring recommendation.



