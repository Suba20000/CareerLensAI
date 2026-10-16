# CareerLens AI 🎯

### AI-Powered Career and Resume Improvement Platform

CareerLens AI is a web application designed to help job seekers understand how their resumes align with job descriptions and identify areas for career improvement.

The project is being developed using Python and Django, with the goal of building a platform that combines resume analysis, job matching, personalised recommendations, and career development tools.

> **Project status:** In development. The current version includes the website interface and basic Django form-submission flow. Advanced resume analysis and AI-powered features are planned for future development.

---

## 📌 Project Overview

Finding a job is not just about having a resume. Job seekers also need to understand what employers are looking for, which skills they already have, and what they can improve.

CareerLens AI aims to make this process easier by helping users compare their resumes against specific job descriptions and work towards their career goals.

## ✨ Planned Features

### 1. Resume Analysis
- Upload a resume for processing.
- Extract relevant information, skills, and experience.
- Identify key qualifications in the resume.

### 2. AI-Powered Job Matching
- Compare resume content with a target job description.
- Generate a job-match score.
- Identify matching skills and potential skill gaps.

### 3. AI Resume Builder
- Generate suggestions to improve resume content.
- Tailor resume wording to a specific job description.
- Allow users to review and approve suggested changes before finalising them.

### 4. Personalised Career Roadmap
- Identify skills that could improve employability.
- Recommend relevant learning resources and projects.
- Suggest practical next steps for career development.

### 5. Progress Tracker
- Track resume versions and analysis results.
- Review improvements over time.
- Help users organise their career development goals.

*These features are planned and will be implemented progressively.*

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Web framework and backend logic |
| HTML | Website structure |
| CSS | Website styling |
| SQLite | Local development database |
| pypdf | PDF text extraction, where implemented |
| Git | Version control |
| GitHub | Source code hosting and project management |
| Power BI | Potential future analytics and visualisation integration |

---

## 🏗️ System Architecture

The planned system follows a web application architecture.

**1. Frontend — User Interface**

HTML and CSS provide the pages users interact with, including the resume upload form, job-description input, and results page.

**2. Backend — Django Application**

Django receives form submissions, validates user inputs, and coordinates the processing required by the application.

**3. Resume Processing**

The planned processing layer will extract text from uploaded resumes and prepare the content for comparison with job descriptions.

**4. AI and Matching Layer**

A future AI integration will analyse resume content in context, identify skill gaps, and generate personalised recommendations.

**5. Database Layer**

SQLite is used for local development. A database such as PostgreSQL may be adopted for deployment and future data-storage requirements.

### Planned Data Flow

User Input → Frontend Form → Django Backend → Resume Processing → AI and Matching → Results Page

*The AI, matching, and persistent-storage components are planned stages, not all implemented features.*

---

## 📂 Project Structure

```text
CareerLensAI/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── home.html
│   │       └── results.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

### What the Main Files Do

- `manage.py` — Runs Django management commands.
- `config/settings.py` — Contains project settings.
- `config/urls.py` — Defines the main URL routing.
- `core/views.py` — Handles requests and application logic.
- `core/urls.py` — Defines URLs for the core application.
- `core/templates/core/home.html` — Contains the main user interface.
- `core/templates/core/results.html` — Displays the results-page interface.
- `core/models.py` — Defines database models when needed.
- `core/migrations/` — Stores database schema changes.
- `requirements.txt` — Lists Python dependencies.
- `.gitignore` — Specifies files Git should not track.

---

## 🚀 Running the Project Locally

### Prerequisites

- Python installed
- Git installed
- Visual Studio Code or another code editor

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Suba20000/CareerLensAI.git
cd CareerLensAI
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the virtual environment**

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**4. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**5. Apply database migrations**

```bash
python manage.py migrate
```

**6. Start the development server**

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

---

## 🗺️ Development Roadmap

- [x] Create the initial Django project structure.
- [x] Build the resume upload and job-description form.
- [x] Create the results-page interface.
- [x] Upload the initial source code to GitHub.
- [ ] Implement and test resume text extraction.
- [ ] Develop resume and job-description matching logic.
- [ ] Integrate an AI model or API.
- [ ] Implement skill-gap analysis and personalised recommendations.
- [ ] Develop the AI resume builder.
- [ ] Add career roadmaps and progress tracking.
- [ ] Add automated tests and improve error handling.
- [ ] Deploy the application online.

---

## 🔒 Privacy and Security

Resumes may contain sensitive personal information. Uploaded resumes and other private user data should be handled securely.

- Do not commit real resumes, API keys, passwords, or secret configuration files to GitHub.
- Validate uploaded files and handle them securely.
- Protect personal information when implementing storage and AI integrations.
- Review Django's production security settings before deployment.

---

## 👩‍💻 About the Project

CareerLens AI is a personal software development project focused on combining web development, resume analysis, and AI-assisted career planning.

The long-term goal is to build a practical platform that helps job seekers understand their strengths, recognise opportunities for improvement, and prepare for their desired roles.

**Repository:** https://github.com/Suba20000/CareerLensAI

**Status:** Work in progress 🚧
