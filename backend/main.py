from tailor_resume import generate_resume
from analyze_candidate import describe_job, get_candidate_job_fit_evaluation

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


def tailor_resume_single_entry(job_posting):
    job_desc = describe_job(job_posting)
    evaluations = get_candidate_job_fit_evaluation(job_desc)
    generate_resume(job_posting, "vsresume", evaluations)

if __name__ == "__main__":
    entry = """The Role


Software Engineer, Agentic AI Systems (New Grad)

Are you a software engineer who has honed your craft through internships, research, and/or academic projects, and are looking to apply your skills at the cutting edge of AI agents? This may be the role for you.

As a software engineer on our “agent lab” Natural Language Understanding team, you will play an important part in our mission: to advance the frontier of work that can be entrusted to agents to perform reliably at scale. You will have the opportunity to contribute to the evolution of the Moveworks AI Assistant platform in several of the following areas: agent orchestration, sandboxed file systems and code execution, latency optimization, agent memory, LLM self-reflection and improvement, execution environment simulation, enterprise knowledge graphs, and multimodal I/O.

You will have all the tools of modern enterprise AI at your disposal, including best-in-class LLMs from providers like OpenAI. Our team indexes on moving fast on scalable infrastructure, solving challenging product and engineering problems, and pushing the envelope of value provided to customers. If you are looking to do impactful work with a bright, dedicated, and impact-driven team alongside you, we’d love to have a conversation.

What You Will Do:

Take on exciting engineering challenges (see areas listed above) to build and evolve capable AI agent systems that are reliable in every sense of the word
Implement frontier AI algorithms and architectures and help productionize them at scale, with support from senior engineers
Use the latest advances in machine learning, LLMs, and AI agents to enhance our products and create delightful user experiences
Execute on projects to create lasting value for all our customers
Hone your craft in writing robust, extensible, readable, and performant code
Partner with subject matter experts across the company including in machine learning, security, product, user experience, and customer success, to learn from each other and build the best enterprise AI product the world has ever seen
Learn from and collaborate with senior engineers and machine learning engineers to build world-class AI systems
What You Bring To The Table:
Strong programming fundamentals and experience building software through coursework, projects, internships, and/or research
Ability to think and communicate clearly about engineering problems and systems
Eagerness to learn, give and receive feedback, and hold yourself to a high standard of operational excellence
Readiness to hit the ground running in a Mac development environment, programming in Python, Golang, and/or Java
Desire to ship at a startup pace with a high degree of ownership
Attention to detail
Drive to ship product improvements with production-grade code (with guidance and iterative development)
Strong appetite for continuous incremental wins and completing challenging projects fast
High level of curiosity about engineering outside of immediate discipline and ongoing desire to learn and stay at the cutting edge of applied AI
Nice To Have:

Internship or research experience building production-quality software
Experience building with LLMs, particularly in iterating on prompts, on model selection, on cognitive architecture design, and on latency/correctness tradeoffs in a data-driven way
Hands-on experience with one or more stages of a machine learning problem-solving lifecycle, such as experiment setup, dataset curation, model training, offline evaluation and error analysis, deployment, and online evaluation
Experience in AI fairness, privacy, permission controls, safety, and/or security
*Our compensation package includes a market competitive salary, equity for all full time roles, exceptional benefits, and, for applicable roles, commissions or bonus plans. 
Ultimately, in determining pay, final offers may vary from the amount listed based on geography, the role’s scope and complexity, the candidate’s experience and expertise, and other factors.

Moveworks Is An Equal Opportunity Employer
*Moveworks is proud to be an equal opportunity employer. We provide employment opportunities without regard to age, race, color, ancestry, national origin, religion, disability, sex, gender identity or expression, sexual orientation, veteran status, or any other characteristics protected by law.

Who We Are 
Moveworks is the Agentic AI Assistant platform that empowers the entire workforce.

Our platform enables employees to converse with all of their business systems through natural language to quickly find answers and automate tasks. Powered by the world's most advanced LLMs, our proprietary models, and a sophisticated Agentic AI platform, we're transforming how work gets done by allowing AI to take initiative, streamline complex workflows, and continuously learn and adapt.

Moveworks is trusted by over 5.5 million employees at more than 350 of the world’s largest companies, including 10% of the Fortune 500, to automate everyday tasks and streamline business operations. Recognized on the Forbes Cloud 100 and AI 50 lists, Moveworks was also named one of Fast Company’s 2025 Most Innovative Companies and Inc’s Best in Business, in the Best in Innovation category. Moveworks was also recognized at Microsoft’s 2025 Partner of the Year and in 2024, received the AI Breakthrough Award.

In December 2025, Moveworks was acquired by ServiceNow, marking a pivotal milestone in our journey to create a single front door to work for all business systems. By combining ServiceNow’s leading workflow automation with Moveworks’ Reasoning Engine and natural language capabilities, we deliver the AI platform for every person and every workflow. Built to go beyond basic summaries to deliver meaningful business impact. Together, our AI acts across enterprise systems to turn conversations into completed work.

By joining our team, you’ll be at the forefront of the AI transformation, backed by the global scale of ServiceNow and the agility of a high-growth company. We are looking for world-class talent to help us extend agentic AI to every employee across every corner of the business.
"""
    tailor_resume_single_entry(entry)