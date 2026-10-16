
from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.exceptions import RequestEntityTooLarge

from analyzer import extract_resume_text
from matcher import analyze_resume

app = Flask(__name__)

# Limit uploaded files to 5 MB.
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {".pdf", ".docx"}


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    uploaded_filename = None
    job_description = ""

    if request.method == "POST":
        resume_file = request.files.get("resume")
        job_description = request.form.get(
            "job_description", ""
        ).strip()

        if not resume_file or not resume_file.filename:
            error = "Please select a resume file."

        elif Path(resume_file.filename).suffix.lower() not in ALLOWED_EXTENSIONS:
            error = "Please upload a PDF or DOCX resume."

        elif not job_description:
            error = "Please enter a job description."

        else:
            uploaded_filename = resume_file.filename

            try:
                # Read the uploaded file into memory.
                # The uploaded resume is not saved to disk.
                file_bytes = resume_file.read()

                resume_text = extract_resume_text(
                    file_bytes,
                    resume_file.filename
                )

                result = analyze_resume(
                    resume_text,
                    job_description
                )

            except ValueError as exc:
                error = str(exc)

    return render_template(
        "index.html",
        result=result,
        error=error,
        uploaded_filename=uploaded_filename,
        job_description=job_description
    )


@app.errorhandler(RequestEntityTooLarge)
def file_too_large(error):
    return render_template(
        "index.html",
        result=None,
        error="The upload exceeds 5 MB. Please choose a smaller file.",
        uploaded_filename=None,
        job_description=""
    ), 413


if __name__ == "__main__":
    app.run(debug=True)
