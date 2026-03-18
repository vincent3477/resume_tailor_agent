import os
import requests
from typing import Any
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-5")

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

def describe_job(job_desc):


    
    prompt = f"""
    Your responsibility is to parse the job data extracting title, and description in order to effectivily summarize the important qualification information and what person would resonate with what the company is looking for from the posting.

    This is the job descripotion: {job_desc}

    Your answer should:
    - list all required skills (i.e. Python, Azure)
    - list all preferred skills and/ or experiences
    - discuss the skills the candidate should emphasize to stand out
    - describe what the company is looking for.
    - describe the company's mission and values
    - describe what the candidate will be doing.
    - how many years of experience does this job require or seniority if the number of years of experience is not listed
    - if prior job or internship is required
    - include the type 

    Your answer must be in this format:
    {{"job title": "<title here>", "All required skills": "<required_skills>", "Preferred Skills": "<preferred_skills>", "skills candidate should emphasize":"<what_to_emphasize>", "Years of experience required":"<years_of_experience_required>", "Whether prior internship or job is required": "<yes if strictly says internship or job only, no otherwise>", "what the company is looking for":<what the company is looking for>, "what will the candidate be doing":<what the candidate will do>, "mission and values":<company's mission and values"}}

    """

    #response = client.responses.create(
    #        model=MODEL,
    #        input=prompt,
    #    )

    url = "https://agents.toolhouse.ai/4c85d8d5-601a-47f5-8425-336f522e2445"

    payload = {"message": f"JOB Description: {job_desc}"}
    api_key = os.environ.get("TOOLHOUSE_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print("about to passin in the request, ", payload)

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.text  # This should be a JSON string
        else:
            print(f"Failed to query agent. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error querying agent: {str(e)}")
        return None


def get_candidate_job_fit_evaluation(broken_down_desc):
    prompt = f"""
    Your job is to analyze a job posting and return structured signals that guide resume tailoring.

You must determine:

1. What the candidate should highlight
2. How the resume should be framed
3. Whether AI/ML, systems, backend, or other domains are required
4. How to prioritize projects, experience, and skills
5. What signals make a strong candidate for this role
6. What should be avoided or de-emphasized

Here is the broken down job description: {broken_down_desc} 

And, here is the candidate's data: {RESUME_DATA}

Return STRICT JSON with fields:

{{
  "role_family": "",
  "seniority": "",
  "company_type": "",

  "domain_requirements": {{
    "ai_ml": true/false,
    "systems": true/false,
    "backend": true/false
  }},

  "project_preferences": {{
    "priority_order": [],
    "must_have_signals": [],
    "deprioritize": []
  }},

  "bullet_preferences": {{
    "emphasize": [],
    "de_emphasize": []
  }},

  "skill_strategy": {{
    "must_include": [],
    "nice_to_have": [],
    "avoid": []
  }},

  "experience_strategy": {{
    "priority_order": [],
    "include_conditions": {{}}
  }},

  "narrative_strategy": {{
    "core_theme": "",
    "angle": "",
    "differentiators": []
  }},

  "risks": {{
    "overemphasis": [],
    "underemphasis": [],
    "missing": []
  }}
}}
"""
    
    

    url = "https://agents.toolhouse.ai/01990a75-2540-47f3-8b10-4bdfbcdc2130"

    payload = {"message": f"Broken Down job Descriotion:{broken_down_desc} \n\n\n User's Data: {RESUME_DATA}"}
    api_key = os.environ.get("TOOLHOUSE_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


    print("about to passin in the request, ", payload)

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Failed to query agent. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error querying agent: {str(e)}")
        return None
