
from django.shortcuts import render
from pypdf import PdfReader
from io import BytesIO
import re


def home(request):
    if request.method == "POST":
        resume = request.FILES.get("resume")
        job_description = request.POST.get("job_description", "").strip()

        if not resume or not job_description:
            return render(request, "core/home.html", {
                "error": "Please upload your resume and enter a job description."
            })

        try:
            if not resume.name.lower().endswith(".pdf"):
                return render(request, "core/home.html", {
                    "error": "Please upload your resume as a PDF file."
                })

            reader = PdfReader(BytesIO(resume.read()))
            resume_text = "\n".join(
                page.extract_text() or "" for page in reader.pages
            ).strip()

            if not resume_text:
                return render(request, "core/home.html", {
                    "error": "No readable text was found. Please try a text-based PDF."
                })

            # Basic keyword matching (not AI analysis yet).
            words = lambda text: set(
                re.findall(r"\b[a-zA-Z][a-zA-Z+#.-]*\b", text.lower())
            )

            resume_words = words(resume_text)
            job_words = words(job_description)

            stop_words = {
                "the", "and", "for", "with", "you", "your", "are",
                "this", "that", "will", "our", "from", "have", "has",
                "who", "what", "when", "where", "how", "into", "their",
                "they", "them", "can", "all", "not", "but", "was",
                "were", "been", "being", "its", "job", "role"
            }

            keywords = {
                word for word in job_words
                if len(word) > 2 and word not in stop_words
            }

            matched = sorted(resume_words & keywords)
            missing = sorted(keywords - resume_words)

            score = round(
                len(matched) / len(keywords) * 100
            ) if keywords else 0

            return render(request, "core/results.html", {
                "resume_name": resume.name,
                "job_description": job_description,
                "match_score": score,
                "matched_keywords": matched,
                "missing_keywords": missing,
                "resume_text": resume_text,
            })

        except Exception:
            return render(request, "core/home.html", {
                "error": "We couldn't read this PDF. Please try another PDF file."
            })

    return render(request, "core/home.html")

    return render(request, "core/home.html")
