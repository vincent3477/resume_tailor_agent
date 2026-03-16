import json
import subprocess
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


def get_resume_limits(job_posting):
    text = job_posting.lower()

    systems_keywords = ["c++", "c ", "memory", "systems", "multithread", "concurrency"]
    backend_keywords = ["backend", "api", "database", "sql", "service"]
    ai_keywords = ["ml", "machine learning", "ai", "llm", "rag", "retrieval", "model"]

    is_systems = any(k in text for k in systems_keywords)
    is_backend = any(k in text for k in backend_keywords)
    is_ai = any(k in text for k in ai_keywords)

    limits = {
        "max_skill_rows": 4,
        "max_items_per_skill_row": 5,
        "max_experience_entries": 2,
        "max_experience_bullets": 3,
        "max_projects": 2,
        "max_project_bullets": 3,
        "max_courses": 3,
    }

    if is_ai:
        limits["max_projects"] = 2

    if is_systems:
        limits["max_projects"] = 1
        limits["max_project_bullets"] = 2

    if is_backend:
        limits["max_projects"] = min(2, limits["max_projects"] + 1)

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


def tailor_resume(job_posting, resume_data):
    prompt = f"""
You are tailoring a resume for a job posting.

Job posting:
{job_posting}

Candidate resume data:
{json.dumps(resume_data, indent=2)}

Rules:

Skills:
- Return 3 to 4 skill rows only.
- Each row must contain at most 5 items.
- Choose only the most relevant technologies for the job posting.
- Do not keyword stuff.
- Prefer skills directly supported by the selected experience and selected projects.
- Use concise labels such as:
  - Languages
  - ML / AI
  - LLM Systems
  - Retrieval / Data
  - Backend / APIs
  - Systems
  - Full-Stack
  - Mobile
- Avoid vague filler categories.

Relevant Courses:
- Return 2 to 4 relevant courses only.
- Only select from the candidate's listed courses.
- Choose courses that best support the target role.

Projects:
- 2 projects must be chosen.
- Prioritize AI and ML projects when relevant.
- Prefer projects with strong overlap with the job posting.

Experience:
- Always include Lab Assistant.
- Include Data Structures and Algorithms Course Tutor only if the role mentions:
  data structures, algorithms, C, C++, systems, memory management, low-level debugging.

Bullets:
- Select the most relevant bullets to the role.
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

    response = client.responses.create(
        model=MODEL,
        input=prompt,
    )

    text = response.output_text
    print(text)
    return json.loads(text)


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
    for proj in tailored["projects"][:2]:
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


def generate_resume(job_posting, output_name):
    base_tailored = tailor_resume(job_posting, RESUME_DATA)
    limits = get_resume_limits(job_posting)

    while True:
        tailored = trim_tailored_content(base_tailored, limits)

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

        tex_file = f"{output_name}.tex"
        pdf_file = f"{output_name}.pdf"

        with open(tex_file, "w", encoding="utf-8") as f:
            f.write(final_tex)

        compile_pdf(tex_file)

        pages = get_pdf_page_count(pdf_file)
        if pages == 1:
            break
    
        

        print("CONTENT IS OVER ONE PAGE.")

        new_limits = shrink_limits(limits)
        if new_limits == limits:
            print("Warning: resume still exceeds one page after all shrink attempts.")
            break
        limits = new_limits

    print("Resume generated:", f"{output_name}.pdf")


if __name__ == "__main__":
    posting = """{
  "job title": "ML / AI Engineer at Ludo Robotics",
  "All required skills": "Machine Learning fundamentals, Deep Learning techniques, experience with ML frameworks such as PyTorch or TensorFlow, strong Python programming skills, familiarity or willingness to work with C++ in robotics environments",
  "Preferred Skills": "Experience working on ambiguous open-ended problems, handling real-world noisy data, familiarity with robotics concepts like perception, control, state estimation, or simulation, strong problem-solving and system design skills, collaboration in a fast-paced research-driven environment, clear communication skills, ownership mindset",
  "skills candidate should emphasize": "The candidate should emphasize their strong Python skills and extensive hands-on experience with PyTorch and TensorFlow through various projects and research. Highlight experience with real-world data, multi-agent systems, and retrieval-augmented generation (RAG) pipelines which relate closely to robotics AI systems. Stress familiarity and comfort with ambiguous, open-ended problems demonstrated by multiple research and project initiatives. Also, mention the proficiency in C++ and multithreaded systems (e.g., HTTP server project) since the role mentions working with C++ based robotics environments. Emphasize teamwork and fast iteration experience shown in hackathons and lab collaboration. Lastly, highlight ownership and impact in projects with real deployments and research-to-application pipeline experience.",
  "Years of experience required": "Not explicitly stated; position may be filled at multiple levels. The job suits candidates ranging from new graduates to experienced engineers.",
  "Whether prior internship or job is required": "No",
  "suggestion to apply": "yes"
}

"""
    
    
    #generate_resume(posting, "new_resume")
    compile_pdf(tex_file="new_resume")