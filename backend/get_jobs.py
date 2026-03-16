import os
import requests
from typing import Any

from openai import OpenAI

"""
THEIRSTACK_API_KEY = os.environ["THEIRSTACK_API_KEY"]
THEIRSTACK_URL = "https://api.theirstack.com/v1/jobs/search"


def search_theirstack_jobs(
    api_key: str,
    titles: list[str],
    location_ids: list[int] | None = None,
    posted_at_max_age_days: int = 7,
    page: int = 0,
    limit: int = 10,
    blur_company_data: bool = False,
    include_total_results: bool = False,
) ->" dict[str, Any]:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload: dict[str, Any] = {
        "job_title_or": titles,
        "posted_at_max_age_days": posted_at_max_age_days,
        "blur_company_data": blur_company_data,
        "page": page,
        "limit": limit,
        "include_total_results": include_total_results,
    }

    if location_ids:
        payload["job_location_or"] = [{"id": loc_id} for loc_id in location_ids]

    response = requests.post(
        THEIRSTACK_URL,
        headers=headers,
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    results = search_theirstack_jobs(
        api_key=THEIRSTACK_API_KEY,
        titles=["machine learning", "context engineer", "ai engineer", "software engineer"],
        location_ids=[6252001],
        posted_at_max_age_days=7,
        page=0,
        limit=10,
    )

    print(results)
    """


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
        ("Machine Learning Concepts:", "Neural Networks, Linear Regression, Logistic Regression, Supervised Learning, Unsupervised Learning"),
        ("MLOps:", "Data Preprocessing, Feature Engineering, Training, Checkpointing, Evaluation, Fine-Tuning"),
        ("Web Development:", "React, Vue, Flask, FastAPI"),
        ("AI Agents:", "RAG, Prompt Engineering, Agent Orchestration, Tool Calling, LangChain, RAGAS"),
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

def describe(job_desc):
    prompt = f"""
    You are a job matching expert that is responsible to for parsing the job data extracting the title, description, pay, and location then determine whether the candidate is good match based on their experiences.

    This is the job descripotion: {job_desc}

    Candidate Data: {RESUME_DATA}

    Your answer should:
    - list all required skills (i.e. Python, Azure)
    - list all preferred skills and/ or experiences
    - discuss the skills the candidate should emphasize to stand out and suggestions to frame their resume to match what the company wants
    - how many years of experience does this job require or seniority if the number of years of experience is not listed
    - if prior job or internship is required
    - include the type 
    - Suggest of the candidate should apply or not.

    Your answer must be in this format:
    {{"job title": "<title here>", "All required skills": "<required_skills>", "Preferred Skills": "<preferred_skills>", "skills candidate should emphasize":"<what_to_emphasize>", "Years of experience required":"<years_of_experience_required>", "Whether prior internship or job is required": "<yes if strictly says internship or job only, no otherwise>", "suggestion to apply":"yes or no"}}

    """


    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


    response = client.responses.create(
            model=MODEL,
            input=prompt,
        )

    text = response.output_text
    print(text)

if __name__ == "__main__":
    describe("""About the job
The Company

LUDO ROBOTICS is dedicated to building general-purpose robotic intelligence systems that are robust, adaptive, and capable of handling real-world scenarios. We believe that data-driven machine learning at massive scale is the key to unlocking these capabilities and enabling the widespread deployment of robots across society.

We are a new startup headquartered in Bay Area, California, with an office in Seoul, Korea. Our team spans a wide range of backgrounds and experience, from new graduates to seasoned domain experts. What matters most to us is ownership, speed, and intellectual curiosity - people who take responsibility, move fast, and enjoy thinking deeply about hard problems.

We are supported by a highly advanced AI Center within KRAFTON, a leading global video game company best known for the genre-defining worldwide success PUBG: Battlegrounds. KRAFTON has extensive experience building and operating large-scale, data-rich products, and we have secured investment from them. This gives us strong long-term backing, deep technical partnership opportunities, and access to world-class infrastructure and talent networks as we push robotic intelligence forward.

We are looking for passionate builders who want to explore uncharted territory, take on difficult problems, and ship ambitious, industry-shaping work. You will collaborate across diverse teams as we bring our technology from research into real-world deployment.

THE OPPORTUNITY

As an ML / AI Engineer at Ludo Robotics, you will develop scalable robotics systems that enable robots to operate reliably in the real-world environments. You will work with leading researchers and engineers on state-of-the-art methodologies to design and deploy algorithms and systems that enable robots to interact intelligently and adapt to diverse and complex environments. The ideal candidate has a strong technical background and experience in building practical solutions and driving real impact.

Responsibilities

Lead and contribute to cutting-edge research and engineering problems at the frontier of robotic AI, including approaches and systems that have not been built before.
Explore and develop new learning methods, architectures, and training strategies for robots facing unseen scenarios.
Turn research ideas into deployed robot behavior, bridging theory and real-world performance.
Collaborate with cross-functional teams spanning robotics software, hardware, data, and infrastructure.
Influence technical direction and system design in a fast-moving startup environment.
Access large-scale data, compute, and modern ML infrastructure to train and evaluate advanced models.
Grow through ownership of open-ended problems where solutions are not predefined.

Qualifications

Degree in Computer Science, Electrical Engineering, or related field with focus on Deep Learning or Machine Learning
Solid understanding of machine learning fundamentals and modern deep learning techniques, with hands-on experience with ML frameworks such as PyTorch or TensorFlow.
Strong programming skills, primarily in Python, with experience or willingness to work in C++-based robotics environments.
Comfort working on open-ended, ambiguous problems where requirements and solutions evolve and curiosity and readiness to tackle new technical challenges that may not have established best practices.
Experience working with real-world data, including noise, edge cases, and imperfect labels.
Familiarity with robotics concepts such as perception, control, state estimation, or simulation a plus.
Strong problem-solving skills and the ability to reason about complex systems.
Ability to collaborate effectively in fast-paced, research-driven environments.
Clear communication skills and a strong sense of ownership over outcomes.

Reasonable Accommodation

LUDO ROBOTICS is committed to the full inclusion of all qualified individuals. As part of this commitment, the Company will ensure that persons with disabilities are provided reasonable accommodations. If reasonable accommodation is needed to apply for an open position, perform essential job functions, and/or to receive other benefits and privileges of employment, please contact the Operations Team, to begin the interactive process.

EEOC Statement

LUDO ROBOTICS provides equal employment opportunities to all employees and applicants for employment and prohibits discrimination and harassment of any type.

This position may be filled at multiple levels depending on experience, scope, and business need. In California, the expected salary range for this position is $98,000–$305,000. The listed expected salary ranges represent good faith estimates. Actual compensation may vary based on job-related factors including experience, education, skills, performance, and work location. This position is also eligible for equity compensation and a comprehensive benefits package.""")
