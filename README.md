**AI Resume Keyword Extractor + Job Match Scorer: Deployment Guide**

This document outlines the procedure for deploying and executing the local AI engine designed for resume text extraction, keyword identification, and job-resume match scoring utilizing Natural Language Processing (NLP) techniques.
The application operates locally using Python and the FastAPI framework, requiring no external API keys or cloud service dependencies
1. Prerequisites and System Requirements
1.1. Required Software and Environment
Software Required:
Python3.11.x 
pip
Uvicorn
Diagnostic Checks
Before project execution, confirm the following system readiness checks.
Python Installation: python --version
pip Utility: pip --version
Virtual Environment Module: python -m venv --help
Port Availability (8000): netstat -ano | findstr :8000


2. Project Setup
2.1. Project Acquisition
Acquire the source code using one of the following methods:
git clone https://github.com/nishaelizabeth2002/AI-Resume-Keyword-Extractor.git
cd AI-Resume-Keyword-Extractor

2.2  Virtual Environment Creation
A dedicated virtual environment (.venv) is mandatory for dependency isolation.
Windows (PowerShell): python -m venv .venv.\.venv\Scripts\Activate.ps1
macOS / Linuxpython3 -m venv .venvsource .venv/bin/activate

2.3 Dependency Installation:
Execute the following command within the activated virtual environment to install all required libraries:
pip install -r requirements.txt
Dependencies Installed: FastAPI, Uvicorn, Pandas, Scikit-learn, PDF/Text Parsers, and NLTK.

2.4 NLTK Data Model Download
The NLP engine requires specific NLTK data models. These must be downloaded prior to execution.
Execute this command within the activated virtual environment:
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet');


3. Application Execution

3.1. API Server Startup
Start the FastAPI application server using the Uvicorn web server. The --reload flag is optional but recommended for development.
uvicorn app.main:app --reload

3.2. Accessing the Web Interface
The interactive web interface and API documentation are accessible via the Swagger UI endpoint after successful server startup.
Open the following URL in a web browser:
👉 http://127.0.0.1:8000/docs


