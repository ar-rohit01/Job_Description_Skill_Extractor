# 📄 Job Description Skill Extractor

> **An AI-powered GenAI application that extracts skills, experience, and education from job descriptions using Gemini, Prompt Engineering, Pydantic, and Streamlit.**

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Google-Gemini-orange?logo=google)](https://ai.google.dev/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Structured%20Output-E92063?logo=pydantic\&logoColor=white)](https://docs.pydantic.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Project Overview

Job descriptions often contain important hiring requirements inside long paragraphs. Manually identifying the required **skills, experience, and education** can be time-consuming.

This project provides a simple AI-powered solution that analyzes a job description and extracts the required information into a **structured and validated format**.

### The application extracts:

* 🛠️ **Skills**
* 💼 **Experience**
* 🎓 **Education**

A key design requirement of this project is:

> **The system must not assume, infer, or generate information that is not explicitly mentioned in the job description.**

---

# 🎯 Problem Statement

Job descriptions contain valuable recruitment information, but the required skills, experience, and education are often embedded within large amounts of text.

For example:

### Input

```text
Looking for a Python developer with 3 years experience.
Skills required: Python, SQL and Git.
Bachelor's degree in Computer Science preferred.
```

### Structured Output

```json
{
  "skills": [
    "Python",
    "SQL",
    "Git"
  ],
  "experience": "3 years experience",
  "education": "Bachelor's degree in Computer Science preferred"
}
```

This makes the information easier to understand and process programmatically.

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Extract explicitly mentioned skills from job descriptions.
2. Extract explicitly mentioned experience requirements.
3. Extract explicitly mentioned education requirements.
4. Prevent the AI from inventing missing information.
5. Return the extracted information in a structured format.
6. Validate the output using Pydantic.
7. Provide a simple user-friendly Streamlit interface.
8. Build the application using a modular architecture.
9. Secure the Gemini API key using environment variables.
10. Prepare the application for cloud deployment.

---

# 🧠 Solution Approach

The application follows a simple GenAI pipeline:

```text
                USER
                  │
                  ▼
        ┌──────────────────┐
        │  Streamlit UI    │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Prompt Template  │
        │  & Instructions  │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Gemini LLM      │
        │   API / Model    │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Pydantic Parser  │
        │  Validation      │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Structured       │
        │ Output           │
        └──────────────────┘
```

---

# ✨ Key Features

### 🔹 Skill Extraction

Extracts skills explicitly mentioned in the job description.

Example:

```text
Python, SQL, Pandas, NumPy, Machine Learning
```

becomes:

```json
"skills": [
  "Python",
  "SQL",
  "Pandas",
  "NumPy",
  "Machine Learning"
]
```

### 🔹 Experience Extraction

Extracts only explicitly stated experience requirements.

Examples:

```text
3 years experience
```

```text
Minimum 2 years of experience
```

```text
5+ years experience
```

If no experience requirement is mentioned:

```text
"not_available"
```

### 🔹 Education Extraction

Extracts explicitly stated education requirements.

Examples:

```text
Bachelor's degree in Computer Science
```

```text
B.Tech in Mechanical Engineering
```

If education is not mentioned:

```text
"not_available"
```

### 🔹 No-Inference Design

The application is specifically instructed **not to invent missing information**.

For example, if a job description says:

```text
We are looking for a Python developer.
```

The system should not automatically assume:

```text
Education: Computer Science degree
Experience: 2 years
```

Instead:

```json
{
  "skills": ["Python"],
  "experience": "not_available",
  "education": "not_available"
}
```

---

# 🧩 Prompt Engineering

A dedicated prompt template is used to control the behavior of the Gemini model.

The prompt defines strict extraction rules for:

* Skills
* Experience
* Education
* Missing information
* No inference
* Explicit information only

The application uses a system instruction rather than relying only on the user input.

This helps make the model's output more consistent with the project requirements.

---

# 📦 Structured Output

The application uses **Pydantic** to define the expected output structure.

```python
class JobDescriptionOutput(BaseModel):
    skills: List[str] = Field(default_factory=list)
    experience: str = "not_available"
    education: str = "not_available"
```

Expected structure:

```json
{
  "skills": ["string"],
  "experience": "string",
  "education": "string"
}
```

This provides a predictable data structure that can be used by other applications or APIs.

---

# 🧪 Testing

The application was tested using multiple types of job descriptions.

## Test Case 1 — Clear Job Description

### Input

```text
Looking for Python developer with 3 years experience
and a Bachelor degree in Computer Science.
Skills required: Python, SQL and Git.
```

### Output

```json
{
  "skills": [
    "Python",
    "SQL",
    "Git"
  ],
  "experience": "3 years experience",
  "education": "Bachelor degree in Computer Science"
}
```

---

## Test Case 2 — Missing Information

### Input

```text
We are looking for a Python developer who can build
data processing scripts.
```

### Output

```json
{
  "skills": [
    "Python",
    "data processing scripts"
  ],
  "experience": "not_available",
  "education": "not_available"
}
```

The application does not invent an education or experience requirement.

---

## Test Case 3 — Multiple Skills

### Input

```text
We are looking for a Data Scientist with 2 years of experience.

Required skills include Python, SQL, Pandas, NumPy,
Scikit-learn, Machine Learning, Deep Learning, NLP,
and Power BI.

Candidates should have a Bachelor's degree in Computer Science,
Data Science, or a related field.
```

### Output

```json
{
  "skills": [
    "Python",
    "SQL",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Power BI"
  ],
  "experience": "2 years of experience",
  "education": "Bachelor's degree in Computer Science, Data Science, or a related field"
}
```

---

# 🛠️ Technologies Used

| Technology             | Purpose                             |
| ---------------------- | ----------------------------------- |
| **Python**             | Application development             |
| **Google Gemini**      | Large Language Model                |
| **Google GenAI SDK**   | Gemini API integration              |
| **Prompt Engineering** | Control extraction behavior         |
| **Pydantic**           | Output schema and validation        |
| **Streamlit**          | User interface                      |
| **python-dotenv**      | Environment variable management     |
| **Git & GitHub**       | Version control and project hosting |

---

# 📁 Project Structure

```text
Job_Description_Skill_Extractor/
│
├── main.py
├── model.py
├── parser.py
├── prompt.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── .env
```

### File Responsibilities

#### `main.py`

The application entry point.

Responsible for:

* Streamlit UI
* User input
* Button interaction
* Displaying structured results
* Error handling

#### `prompt.py`

Contains the system instructions used for the LLM.

Responsible for:

* Extraction rules
* No-inference instructions
* Missing-field behavior
* Output expectations

#### `model.py`

Handles communication with the Gemini API.

Responsible for:

* Loading API credentials
* Creating the Gemini client
* Sending the job description
* Requesting structured JSON output
* Returning validated results

#### `parser.py`

Contains the Pydantic output model.

Responsible for defining the expected structure:

```text
skills
experience
education
```

---

# 🔐 Environment Variables

The Gemini API key is stored in an environment file instead of being hardcoded in the source code.

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore`.

```text
.env
.venv/
__pycache__/
*.pyc
```

> 🔒 **The API key should never be committed to GitHub.**

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ar-rohit01/Job_Description_Skill_Extractor.git
```

## 2. Navigate to the Project

```bash
cd Job_Description_Skill_Extractor
```

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate the Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Configure the API Key

Create `.env`:

```text
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run main.py
```

The application will open in the browser.

---

# 🖥️ Application Interface

The application provides a simple interface where the user can:

1. Paste a job description.
2. Click **Extract Information**.
3. View extracted skills.
4. View experience.
5. View education.

### Example Flow

```text
Paste Job Description
        ↓
Click Extract Information
        ↓
Gemini processes the text
        ↓
Pydantic validates the output
        ↓
Structured information displayed
```

---

# ☁️ Deployment

The application is designed for deployment using **Streamlit Community Cloud**.

Deployment requirements include:

* GitHub repository
* `requirements.txt`
* Streamlit entry point
* Gemini API key configured as a deployment secret

The API key is **not stored in the GitHub repository**.

---

# 🏗️ Architecture Design

The project follows a modular architecture:

```text
┌─────────────────────────────┐
│        Streamlit UI         │
│          main.py            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Prompt Template        │
│         prompt.py           │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│        Gemini Model         │
│          model.py           │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Pydantic Validation      │
│          parser.py          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Structured Result      │
│ skills / experience /       │
│ education                   │
└─────────────────────────────┘
```

---

# 💡 Why This Project?

This project demonstrates practical implementation of several important GenAI concepts:

* Large Language Models
* Prompt Engineering
* Structured Generation
* Pydantic Schema Validation
* API Integration
* Environment Variable Security
* Streamlit Application Development
* Error Handling
* Modular Python Architecture
* Git/GitHub Workflow
* Cloud Deployment

Rather than simply sending a prompt to an LLM, the application combines **prompt constraints + structured output + validation** to make the result more predictable and usable.

---

# 🚧 Challenges & Solutions

| Challenge                                       | Solution                                          |
| ----------------------------------------------- | ------------------------------------------------- |
| LLM generated information not present in the JD | Added strict no-inference system instructions     |
| Unstructured LLM responses                      | Used Pydantic structured output                   |
| API key security                                | Stored key in `.env`                              |
| Missing information                             | Defined `not_available` behavior                  |
| Different job descriptions                      | Tested clear, missing-field and multi-skill cases |
| User interaction                                | Built Streamlit interface                         |
| Deployment security                             | API key configured through deployment secrets     |

---

# 🔮 Future Improvements

Possible future enhancements include:

* 📊 Skill categorization
* 🧠 Skill normalization
* 📈 Job-to-candidate matching
* 📄 Resume parsing
* 🔍 Job description comparison
* 📊 Skill demand analysis
* 🗂️ Multiple job description processing
* 💾 Database storage
* 📥 Export results to CSV/JSON
* 🔐 User authentication
* 🌐 REST API using FastAPI
* 🤖 Agent-based recruitment workflows

---

# 📚 Project Requirements Covered

This project addresses the major requirements of the GenAI project workflow:

### Sprint 1

* ✅ Problem understanding
* ✅ Input definition
* ✅ Structured output definition
* ✅ Business use case
* ✅ Prompt design
* ✅ Pydantic schema
* ✅ Modular application architecture
* ✅ Streamlit interface
* ✅ Multiple test cases
* ✅ Edge-case testing

### Sprint 2

* ✅ Dependency management
* ✅ `requirements.txt`
* ✅ Environment variable handling
* ✅ API key security
* ✅ Deployment-ready application

### Sprint 3

* 📌 Project report
* 📌 Presentation
* 📌 Demo
* 📌 Viva preparation

---

# 👨‍💻 Author

## Rohit Rajaram Yadav

**B.Tech — Automation & Robotics Engineering**

### Areas of Interest

* Artificial Intelligence
* Machine Learning
* Data Science
* Generative AI
* Deep Learning
* Computer Vision
* Intelligent Automation

### Connect With Me

🔗 **LinkedIn:**
https://www.linkedin.com/in/rohit-yadav-6b8999299

💻 **GitHub:**
https://github.com/ar-rohit01

---

# ⭐ Project Repository

**Job Description Skill Extractor**

🔗 https://github.com/ar-rohit01/Job_Description_Skill_Extractor

---

## 📌 Project Summary

**Job Description Skill Extractor** is a GenAI-powered application that transforms unstructured job descriptions into structured hiring information.

```text
Job Description
      ↓
Prompt Engineering
      ↓
Gemini LLM
      ↓
Structured JSON
      ↓
Pydantic Validation
      ↓
Skills + Experience + Education
```

> **Built with Python, Gemini, Prompt Engineering, Pydantic and Streamlit.**
