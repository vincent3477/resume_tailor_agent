import json
import subprocess
import requests
import os
from openai import OpenAI



client = OpenAI()

MODEL = "gpt-5"

RESUME_DATA = {
    "name": "Vincent Siu",
    "location": "San Leandro, CA",
    "email": "vincent.siu.0101@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/vincentsiu3477/",
    "linkedin_text": "linkedin.com/in/vincentsiu3477",
    "github_url": "https://github.com/vincent3477",
    "github_text": "github.com/vincent3477",
    "degree": "Bachelors of Computer Science",
    "education_dates": "September 2021 - June 2025",
    "school": "University of California Santa Cruz",
    "gpa": "3.51",
    "courses": [
        "Artificial Intelligence",
        "Applied Machine Learning",
        "Natural Language Processing",
        "Data Structures and Algorithms",
        "Software Engineering",
        "Building Web Applications",
        "Deep Learning",
        "Machine Learning"
    ],
    "certifications": [
        {
            "name": "Microsoft AI-900 Azure AI Fundamentals",
            "date": "Earned January 2026",
        }
    ],
    "skills_rows": [
        ("Languages:", "Python, C, C++, Java, JavaScript, SQL, HTML/CSS"),
        ("Machine Learning Concepts:", "Neural Networks, Linear Regression, Logistic Regression, Supervised Learning, Unsupervised Learning, LLM"),
        ("MLOps:", "Data Preprocessing, Feature Engineering, Training, Checkpointing, Evaluation, Fine-Tuning"),
        ("Web Development:", "React, Vue, Flask, FastAPI"),
        ("AI Agents:", "RAG, Prompt Engineering, Agent Orchestration, Tool Calling, LangChain, RAGAS, Context Engineering"),
        ("Machine Learning Libraries:", "PyTorch, TensorFlow, Hugging Face Transformers"),
        ("Data & Vector Systems:", "FAISS, Vector Databases, DuckDB, Semantic Retrieval"),
        ("Cloud:", "Microsoft Azure, Google Cloud Platform"),
        ("Computer Design Principles:", "Multi-threading, Race Conditions, Mutexes, Semaphores"),
        ("Software Engineering:", "Git, Debugging, Agile Collaboration, CI/CD Concepts"),
    ],
    "experience": [
        {
            "title": "Lab Assistant",
            "dates": "April 2025 - Present",
            "org": "AIEA Lab UCSC",
            "location": "Santa Cruz, CA",
            "tags": [
                "AI", "ML", "LLM", "RAG", "retrieval", "FAISS", "BERT",
                "vector database", "DuckDB", "SQL", "multi-agent", "evaluation"
            ],
            "bullets": [
                "Built and iterated on an end-to-end persona-based RAG pipeline in Python to ingest, retrieve, and re-rank information from a 6 million-document corpus, improving LLM factual accuracy.",
                "Built semantic retrieval pipeline using 768-D BERT embeddings and FAISS vector DB to surface the most relevant information to be fed to LLM agents.",
                "Designed a modular multi-agent architecture with OpenAI Agents SDK where prompt-engineered agents handled retrieval, validation, re-ranking, refinement, and profile updates.",
                "Implemented SQL queries to retrieve original articles in indexed batches following semantic retrieval, enabling efficient mapping from embedding matches back to source documents.",
                "Used DuckDB-backed article and metadata retrieval workflows to efficiently map semantic matches back to source records for downstream generation.",
                "Designed small-scale experiments using RAGAS, performing A/B testing on prompt variants, comparing parametric vs. article-grounded responses in faithfulness and accuracy. Achieved 90% pipeline response accuracy."
            ],
        },
        {
            "title": "Data Structures and Algorithms Course Tutor",
            "dates": "October 2023 - March 2025",
            "org": "UC Santa Cruz",
            "location": "Santa Cruz, CA",
            "tags": [
                "data structures", "algorithms", "C", "C++",
                "debugging", "memory management", "systems"
            ],
            "bullets": [
                "Assisted students in debugging C and C++ implementations of data structures and algorithms.",
                "Provided guidance on pointer safety, memory management, and sound data structure design.",
                "Explained technical concepts through diagrams and step-by-step reasoning to help students understand implementation requirements.",
                "Supported students in identifying logic bugs, edge cases, and runtime issues in low-level programming assignments."
            ],
        }
    ],
    "projects": [
        {
            "title": "Mentorra (Backend)",
            "subtitle": "Global 500 x PDD Hackathon",
            "tech": "Python, Vector DB, ElevenLabs, Agentic Systems, PromptDriven.ai (using OpenAI API), Prompt Engineering",
            "tags": [
                "AI", "LLM", "agents", "agentic systems", "routing",
                "OpenAI API", "vector database", "backend", "voice AI"
            ],
            "priority_group": "ai_ml",
            "bullets": [
                "Rapidly prototyped and deployed an AI mentor platform that routes user queries through specialized mentor agents, automating structured advisory workflows (strategy, operations, growth).",
                "Prompt engineered a router agent using ToolHouse to dynamically select specialized mentor agents, enforce consistent JSON output formats, and support scalable agent orchestration.",
                "Integrated the ElevenLabs API for real-time voice input and output; awarded Best Use of ElevenLabs."
            ],
        },
        {
            "title": "GradPath Support Platform (Full-Stack)",
            "subtitle": "CalHacks 12.0",
            "tech": "Python, JavaScript, React, Flask, FastAPI, Vector DB, LLM Driven Agents, REST APIs, AI Integration",
            "tags": [
                "full-stack", "AI", "LLM", "agents", "React", "FastAPI",
                "Flask", "ChromaDB", "REST APIs", "matching", "backend", "frontend"
            ],
            "priority_group": "ai_ml_fullstack",
            "bullets": [
                "Owned the development of a full-stack mentorship and learning network platform for recent college graduates.",
                "Utilized Claude to accelerate development; rapidly prototyped a ChromaDB-powered real-time peer matching system (sub 250ms response time) reducing development time by 60%.",
                "Designed and quickly iterated on an integrated ToolHouse agent to help users break down high-level goals into actionable tasks with structured outputs; achieved 90% output consistency.",
                "Built the frontend using React and integrated the peer matching system and ToolHouse agent with REST APIs."
            ],
        },
        {
            "title": "Food Quality Recognizer Website (Full-Stack)",
            "subtitle": "Personal Project",
            "tech": "TensorFlow, Machine Learning, Neural Networks, Python, JavaScript, REST APIs, Flask, Web Development",
            "tags": [
                "AI", "ML", "computer vision", "TensorFlow", "full-stack",
                "Flask", "REST APIs", "JavaScript", "web development"
            ],
            "priority_group": "ai_ml_fullstack",
            "bullets": [
                "Independently designed and developed a full-stack ML recommendation system for casual cooks.",
                "Developed and trained a TensorFlow neural network model with Python for image classification, and iteratively fine-tuned it, achieving over 80% accuracy through hyperparameter tuning.",
                "Integrated the JavaScript, HTML, and CSS frontend with the Python Flask backend through RESTful APIs to support model maintainability and reusability."
            ],
        },
        {
            "title": "Supervised Data Analysis on an Unknown Dataset",
            "subtitle": "Academic Project",
            "tech": "Python, Logistic Regression, Pandas, NumPy, Scikit-learn, Data Engineering, Feature Engineering",
            "tags": [
                "ML", "data analysis", "scikit-learn", "pandas",
                "numpy", "feature engineering", "EDA"
            ],
            "priority_group": "ai_ml",
            "bullets": [
                "Developed a data-cleaning pipeline to engineer productive features using one-hot encoding, type conversion, and imputation of missing values with Pandas and NumPy on messy datasets.",
                "Conducted exploratory data analysis and used Matplotlib to identify feature correlations.",
                "Applied machine learning models including K-Nearest Neighbors, Logistic Regression, and Decision Trees to model relationships between labels, achieving about 90% recall and precision with Logistic Regression."
            ],
        },
        {
            "title": "Food Safety Live Glove Detection (Back-End)",
            "subtitle": "SCAI No Limits Competition - 1st Place",
            "tech": "Python, TensorFlow, Realtime Detection Systems, Neural Network, Deep Learning",
            "tags": [
                "AI", "ML", "computer vision", "TensorFlow",
                "deep learning", "real-time inference", "backend"
            ],
            "priority_group": "ai_ml",
            "bullets": [
                "Collaborated on a scalable detection ML training workflow to identify hygiene violations (glove usage and non-usage) from a dataset of 5,800 images, enabling real-time alerts in operational settings.",
                "Designed and trained a neural network detection model from the 5,800-image dataset with TensorFlow to identify violations in hygienic food-handling practices.",
                "Designed a GIOU loss benchmark and performed tuning to improve detection accuracy for real-time inference scenarios, achieving 90% accuracy."
            ],
        },
        {
            "title": "AI-Generated Image Watermark Generator and Tamper Classifier",
            "subtitle": "CruzHacks 2025",
            "tech": "Python, PyTorch, Convolutional Neural Networks, Supervised Learning, Cross-Team Collaboration",
            "tags": [
                "AI", "ML", "computer vision", "PyTorch", "CNN",
                "supervised learning", "data pipeline", "image processing"
            ],
            "priority_group": "ai_ml",
            "bullets": [
                "Engineered a data pipeline with Python to train a PyTorch-powered watermark tamper detection CNN model by performing image scraping, ingesting over 2,000 raw images, extracting DCT-based NumPy features, and developing model checkpoints.",
                "Achieved 80% accuracy through fine-tuning in 12 hours.",
                "Developed a compact training and experimentation workflow for detecting tampered AI-generated imagery."
            ],
        },
        {
            "title": "AI Powered Calorie Intake Tracker App (Full Stack)",
            "subtitle": "Personal Project",
            "tech": "Python, Swift, TensorFlow, TFLite, Xcode, Intuitive UI Design, Production-ready Systems",
            "tags": [
                "AI", "ML", "mobile", "iOS", "Swift",
                "TensorFlow", "TFLite", "computer vision", "full-stack"
            ],
            "priority_group": "ai_ml_mobile",
            "bullets": [
                "Independently designed and developed an iOS application with Swift and Xcode that identifies the food users consumed, reducing manual logging.",
                "Trained and iteratively fine-tuned a TensorFlow CNN model with Python, achieving over 80% precision and recall, then converted it to TFLite for quick inferences.",
                "Integrated the model with the iOS camera using AVFoundation for real-time image processing.",
                "Designed an intuitive and modular UI and integrated Core Data to support quick user decision-making."
            ],
        },
        {
            "title": "UC Universe (Front-End)",
            "subtitle": "Course Project",
            "tech": "Software Engineering Principles, Agile, Project Management, Cross-Team Collaboration, Version Control",
            "tags": [
                "frontend", "software engineering", "agile",
                "collaboration", "project management"
            ],
            "priority_group": "software",
            "bullets": [
                "Collaborated with 4 teammates to develop a pixel-based game covering 8+ UC campuses to make college research more engaging for prospective students.",
                "Worked within a SCRUM-style workflow and participated in weekly standup meetings.",
                "Contributed to cross-team coordination and iterative feature development."
            ],
        },
        {
            "title": "Multi-Threaded HTTP Server",
            "subtitle": "Course Project",
            "tech": "C, pthreads, Multi-Threading, Concurrency, Systems Design, Backend Systems",
            "tags": [
                "C", "systems", "backend", "multithreading",
                "concurrency", "mutex", "reader writer locks"
            ],
            "priority_group": "systems",
            "bullets": [
                "Designed a multithreaded HTTP server in C that can handle concurrent GET and PUT requests.",
                "Developed a thread pool to efficiently handle multiple file I/O requests of up to 1GB each, using mutexes to enable safe concurrent access to shared resources.",
                "Implemented reader and writer locks to prevent race conditions when accessing shared resources."
            ],
        },
        {
            "title": "Pacman Multi-Agent Search",
            "subtitle": "Coursework",
            "tech": "Python, Artificial Intelligence, Reinforcement Learning, CSPs, Heuristic Development",
            "tags": [
                "AI", "reinforcement learning", "search",
                "multi-agent", "Python", "heuristics"
            ],
            "priority_group": "ai_ml",
            "bullets": [
                "Developed autonomous Pacman agents using reinforcement learning and adversarial search techniques including Minimax, Alpha-Beta, Q-Learning, and Expectimax in Python.",
                "Implemented evaluation functions to balance food seeking, ghost avoidance, and risk-reward tradeoffs.",
                "Implemented recursive tree search with depth limits, simulating multiple agents with both deterministic and stochastic behaviors."
            ],
        }
    ],
}


def escape_latex(text):
    if not isinstance(text, str):
        text = str(text)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        ">": r"\textless",
        "<": r"\textgreater"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def normalize_skill_label(label):
    label = label.strip()
    if not label.endswith(":"):
        label += ":"
    return label


def prune_skills_rows(skills_rows, max_rows=4, max_items_per_row=5):
    pruned = []

    for row in skills_rows[:max_rows]:
        if not isinstance(row, (list, tuple)) or len(row) != 2:
            continue

        label, values = row
        label = normalize_skill_label(str(label))

        items = [item.strip() for item in str(values).split(",") if item.strip()]
        items = items[:max_items_per_row]

        if not items:
            continue

        pruned.append((label, ", ".join(items)))

    return pruned


def get_resume_limits(job_analysis=None):
    limits = {
        "max_skill_rows": 4,
        "max_items_per_skill_row": 5,
        "max_experience_entries": 2,
        "max_experience_bullets": 3,
        "max_projects": 2,
        "max_project_bullets": 3,
        "max_courses": 3,
    }

    if not job_analysis:
        return limits

    role_family = job_analysis.get("role_family", "")
    domain_requirements = job_analysis.get("domain_requirements", {})

    needs_ai = domain_requirements.get("ai_ml", False)
    needs_systems = domain_requirements.get("systems", False)
    needs_backend = domain_requirements.get("backend", False)

    if role_family == "systems" or needs_systems:
        limits["max_projects"] = 1
        limits["max_project_bullets"] = 2

    elif role_family == "ai_ml" or needs_ai:
        limits["max_projects"] = 2
        limits["max_project_bullets"] = 3

    elif role_family == "backend" or needs_backend:
        limits["max_projects"] = 2
        limits["max_project_bullets"] = 3

    return limits

def trim_tailored_content(tailored, limits):
    trimmed = {
        "skills_rows": tailored.get("skills_rows", [])[:limits["max_skill_rows"]],
        "relevant_courses": tailored.get("relevant_courses", [])[:limits["max_courses"]],
        "experience": [],
        "projects": [],
    }

    skill_rows = []
    for row in trimmed["skills_rows"]:
        if not isinstance(row, (list, tuple)) or len(row) != 2:
            continue
        label, values = row
        items = [x.strip() for x in str(values).split(",") if x.strip()]
        items = items[:limits["max_items_per_skill_row"]]
        if items:
            skill_rows.append([label, ", ".join(items)])
    trimmed["skills_rows"] = skill_rows

    for exp in tailored.get("experience", [])[:limits["max_experience_entries"]]:
        trimmed["experience"].append({
            "title": exp.get("title", ""),
            "org": exp.get("org", ""),
            "location": exp.get("location", ""),
            "dates": exp.get("dates", ""),
            "bullets": exp.get("bullets", [])[:limits["max_experience_bullets"]],
        })

    for proj in tailored.get("projects", [])[:limits["max_projects"]]:
        trimmed["projects"].append({
            "title": proj.get("title", ""),
            "subtitle": proj.get("subtitle", ""),
            "tech": proj.get("tech", ""),
            "bullets": proj.get("bullets", [])[:limits["max_project_bullets"]],
        })

    return trimmed


def shrink_limits(limits):
    new_limits = dict(limits)

    if new_limits["max_projects"] > 1:
        new_limits["max_projects"] -= 1
        return new_limits

    if new_limits["max_project_bullets"] > 2:
        new_limits["max_project_bullets"] -= 1
        return new_limits

    if new_limits["max_skill_rows"] > 3:
        new_limits["max_skill_rows"] -= 1
        return new_limits

    if new_limits["max_courses"] > 2:
        new_limits["max_courses"] -= 1
        return new_limits

    if new_limits["max_experience_bullets"] > 2:
        new_limits["max_experience_bullets"] -= 1
        return new_limits

    if new_limits["max_items_per_skill_row"] > 4:
        new_limits["max_items_per_skill_row"] -= 1
        return new_limits

    return new_limits


def get_pdf_page_count(pdf_file):
    result = subprocess.run(
        ["pdfinfo", pdf_file],
        capture_output=True,
        text=True,
        check=True
    )
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":")[1].strip())
    return 0


def tailor_resume(job_posting, resume_data, job_analysis):
    """prompt = f
You are tailoring a resume for a job posting.

Job posting:
{job_posting}

Structured job analysis:
{json.dumps(job_analysis, indent=2)}

Candidate resume data:
{json.dumps(resume_data, indent=2)}

Use the structured job analysis as the primary source of truth for:
- what domains matter
- what projects to prioritize
- what skills to emphasize
- how to frame the candidate
- what to de-emphasize

Rules:

Skills:
- Return 3 to 4 skill rows only.
- Each row must contain at most 5 items.
- Follow the skill_strategy from the structured job analysis.
- Prefer skills directly supported by the selected experience and selected projects.
- Do not keyword stuff.

Relevant Courses:
- Return 2 to 4 relevant courses only.
- Only select from the candidate's listed courses.

Projects:
- Select projects according to project_preferences.priority_order.
- Select 2 to 4 projects.
- Note that experiences including Lab Assistant and Tutor/ Reader roles do not belong here.
- Order selected projects from most relevant to least relevant.
- Prefer projects that match must_have_signals.
- Deprioritize projects matching deprioritize signals.
- Include numbers to signify impact whenever possible.


Experience:
- Follow experience_strategy.priority_order.
- Include or exclude experience based on experience_strategy.include_conditions.

Bullets:
- Order bullets from most important to least important.
- Emphasize bullet_preferences.emphasize.
- De-emphasize bullet_preferences.de_emphasize.
- 2 to 4 bullets per experience/project entry.

Return STRICT JSON in exactly this structure:
{{
  "skills_rows": [
    ["Languages:", "Python, SQL, JavaScript"],
    ["Systems:", "C, C++, Multithreading, Mutexes"],
    ["Backend / APIs:", "FastAPI, Flask, REST APIs"]
  ],
  "relevant_courses": [
    "Data Structures and Algorithms",
    "Artificial Intelligence"
  ],
  "experience": [
    {{
      "title": "",
      "org": "",
      "location": "",
      "dates": "",
      "bullets": []
    }}
  ],
  "projects": [
    {{
      "title": "",
      "subtitle": "",
      "tech": "",
      "bullets": []
    }}
  ]
}}
"""
    
    url = "https://agents.toolhouse.ai/83a7cc26-b690-41b3-b57d-f8131e7dcf55"

    payload = {"message": f"""Job posting:
{job_posting}

Structured job analysis:
{json.dumps(job_analysis, indent=2)}

Candidate resume data:
{json.dumps(resume_data, indent=2)}"""}
    api_key = os.environ.get("TOOLHOUSE_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print("about to passin in the request, ", payload)

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)  # This should be a JSON string
        else:
            print(f"Failed to query agent. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error querying agent: {str(e)}")
        return None



def apply_overflow_formatting(tex, stage):
    """
    stage 0: no change
    stage 1: tighten lists
    stage 2: shrink margins
    stage 3: tighten line spacing
    """

    print("APPLY OVERFLOW FORMATTING APPLIED")

    updated = tex

    if stage >= 1:
        updated = updated.replace(
            "\\begin{itemize}",
            "\\begin{itemize}\n\\itemsep -4pt\n\\parsep 0pt\n\\topsep 0pt"
        )

    if stage >= 2:
        updated = updated.replace(
            "\\usepackage[left=0.4 in,top=0.4in,right=0.4 in,bottom=0.4in]{geometry}",
            "\\usepackage[left=0.32in,top=0.32in,right=0.32in,bottom=0.32in]{geometry}"
        )

    if stage >= 3 and "\\linespread{0.97}\\selectfont" not in updated:
        updated = updated.replace(
            "\\begin{document}",
            "\\begin{document}\n\\linespread{0.97}\\selectfont",
            1
        )

    return updated


def remove_bullet_from_least_relevant_project(tailored, removals=1):
    """
    Assumes projects are ordered from most relevant to least relevant.
    Removes bullets from the last project, but never drops below 1 bullet.
    """

    print("REMOVING BULLET FROM LEAST RELEVANT PROJECTS. ")

    updated = json.loads(json.dumps(tailored))

    projects = updated.get("projects", [])
    if not projects:
        return updated

    least_relevant_project = projects[-1]
    bullets = least_relevant_project.get("bullets", [])

    while removals > 0 and len(bullets) > 1:
        bullets.pop()
        removals -= 1

    least_relevant_project["bullets"] = bullets
    return updated


def apply_overflow_content_stage(tailored, stage):
    """
    stage 0-3: no content removal
    stage 4: remove 1 bullet from least relevant project
    stage 5: remove 2 bullets total from least relevant project
    """
    if stage <= 3:
        return tailored
    if stage == 4:
        return remove_bullet_from_least_relevant_project(tailored, removals=1)
    if stage >= 5:
        return remove_bullet_from_least_relevant_project(tailored, removals=2)
    return tailored


def build_skills_section(skills_rows, limits=None):
    max_rows = 4 if limits is None else limits["max_skill_rows"]
    max_items = 5 if limits is None else limits["max_items_per_skill_row"]
    rows = prune_skills_rows(skills_rows, max_rows=max_rows, max_items_per_row=max_items)

    latex = []
    for left, right in rows:
        safe_left = str(left).replace("&", r"\&")
        safe_right = escape_latex(right)
        latex.append(rf"\textbf{{{safe_left}}} {safe_right} \\")
    return "\n".join(latex)


def build_courses_text(relevant_courses, fallback_courses, limits=None):
    max_courses = 3 if limits is None else limits["max_courses"]
    selected = relevant_courses[:max_courses] if relevant_courses else fallback_courses[:max_courses]
    return ", ".join(escape_latex(course) for course in selected)


def generate_dynamic_sections(tailored):
    latex = []

    latex.append("\\begin{rSection}{RELEVANT EXPERIENCE}")
    for job in tailored["experience"]:
        latex.append(
            f"\\textbf{{{escape_latex(job['title'])}}} \\hfill {escape_latex(job['dates'])}\\\\"
        )
        latex.append(
            f"{escape_latex(job['org'])} \\hfill \\textit{{{escape_latex(job['location'])}}}"
        )
        latex.append("\\begin{itemize}")
        for bullet in job["bullets"][:4]:
            latex.append(f"\\item {escape_latex(bullet)}")
        latex.append("\\end{itemize}")
    latex.append("\\end{rSection}")

    latex.append("\\begin{rSection}{PROJECTS}")
    for proj in tailored["projects"]:
        latex.append(
            f"\\textbf{{{escape_latex(proj['title'])}}}\\hfill{{{escape_latex(proj['subtitle'])}}}\\\\"
        )
        latex.append(escape_latex(proj["tech"]))
        latex.append("\\begin{itemize}")
        for bullet in proj["bullets"][:4]:
            latex.append(f"\\item {escape_latex(bullet)}")
        latex.append("\\end{itemize}")
    latex.append("\\end{rSection}")

    return "\n".join(latex)


def compile_pdf(tex_file):
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_file],
        check=True
    )


def generate_resume(job_posting, output_name, job_analysis):
    base_tailored = tailor_resume(job_posting, RESUME_DATA, job_analysis)
    

    limits = get_resume_limits(job_analysis)

    overflow_stage = 0

    while True:
        tailored = trim_tailored_content(base_tailored, limits)
        tailored = apply_overflow_content_stage(tailored, overflow_stage)

        skills_tex = build_skills_section(tailored.get("skills_rows", []), limits)
        courses_tex = build_courses_text(
            tailored.get("relevant_courses", []),
            RESUME_DATA["courses"],
            limits
        )
        dynamic_tex = generate_dynamic_sections(tailored)

        with open("resume_faangpath.tex") as f:
            template = f.read()

        final_tex = template
        final_tex = final_tex.replace("<<SKILLS_CONTENT>>", skills_tex)
        final_tex = final_tex.replace("<<COURSES_CONTENT>>", courses_tex)
        final_tex = final_tex.replace("<<DYNAMIC_CONTENT>>", dynamic_tex)

        final_tex = apply_overflow_formatting(final_tex, overflow_stage)

        tex_file = f"{output_name}.tex"
        pdf_file = f"{output_name}.pdf"

        with open(tex_file, "w", encoding="utf-8") as f:
            f.write(final_tex)

        compile_pdf(tex_file)

        pages = get_pdf_page_count(pdf_file)
        if pages == 1:
            break

        print("CONTENT IS OVER ONE PAGE.")

        if overflow_stage < 5:
            overflow_stage += 1
            continue

        new_limits = shrink_limits(limits)
        if new_limits == limits:
            print("Warning: resume still exceeds one page after all shrink attempts.")
            break

        limits = new_limits

    print("Resume generated:", f"{output_name}.pdf")

