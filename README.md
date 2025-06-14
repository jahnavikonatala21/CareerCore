# 🧠 CareerCore

[![Python-Version-3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit-Version-1.0+](https://img.shields.io/badge/Streamlit-1.0+-brightgreen.svg)](https://streamlit.io)
[![License-MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> The core components of a career profile, powered by AI.

CareerCore is an AI-powered resume screening and job match analysis tool. It helps job seekers analyze their resumes against job descriptions to evaluate alignment, highlight missing skills, and recommend enhancements for better job match scores.


*(You should replace this with a real screenshot of your app)*

---

## 📋 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Acknowledgements](#-acknowledgements)
- [Contact](#-contact)

---

## 🎯 About The Project

This project was developed as part of the Microsoft Azure AI Internship with the Edunet Foundation to demonstrate the practical application of Natural Language Processing (NLP) for enhancing career readiness.

The application leverages two distinct NLP techniques:
1.  **Named Entity Recognition (NER)**: Using a custom-trained spaCy model to extract specific skills (keywords) from both the resume and the job description.
2.  **Semantic Similarity**: Using Sentence Transformers to analyze the contextual meaning and relevance between the resume's experience and the job's responsibilities, going beyond simple keyword matching.

The final "Overall Match Score" is a weighted average of these two analyses, providing a more holistic view of a candidate's fit for a role.

---

## ✨ Key Features

- **📄 PDF Resume Parsing**: Upload your resume for automated text extraction.
- **📋 Job Description Input**: Paste any job description to assess compatibility.
- **📊 AI-Powered Analysis**:
  - **Overall Match Score**: A weighted score indicating your profile's alignment with the job.
  - **Keyword Match**: Percentage based on skills explicitly found in both documents.
  - **Context Match**: Semantic analysis of how well the meaning of your resume matches the job.
- **💡 Actionable Recommendations**: Get AI-driven suggestions to:
  - Weave in missing skills.
  - Rephrase experience to improve contextual alignment.
- **✅ Skill Gap Analysis**: Clearly see which required skills you have and which you are missing.

---

## 🛠️ Tech Stack

This project is built with a modern Python stack for NLP and web deployment:

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend/Core Logic**: Python
- **NLP & Data Processing**:
  - [spaCy](https://spacy.io/): For Named Entity Recognition (NER) to extract skills.
  - [Sentence-Transformers](https://www.sbert.net/): For generating sentence embeddings and calculating semantic similarity.
  - [PyPDF2](https://pypdf2.readthedocs.io/): For extracting text from PDF resumes.
  - [NumPy](https://numpy.org/): For numerical operations.

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.9+
- `pip` and `venv`
- Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jahnavikonatala21/CareerCore.git
    cd CareerCore
    ```

2.  **Create and activate a virtual environment:**
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the spaCy model:**
    The application uses the `en_core_web_lg` model. Download it by running:
    ```bash
    python -m spacy download en_core_web_lg
    ```

5.  **Ensure `skills.jsonl` is present:**
    This file contains the custom skill patterns for the NER model. Make sure it is in the root directory of the project.

6.  **Launch the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    Your browser should open with the app running at `http://localhost:8501`.

---

## 🖥️ Usage

1.  Open the application in your browser.
2.  Click "Browse files" to upload your resume in PDF format.
3.  Paste the full job description into the text area on the right.
4.  Click the **"Analyze with AI"** button.
5.  Review your "Analysis Report," which includes your overall score, skill breakdown, and personalized recommendations.

#### Sample Output

![Screenshot 2025-06-12 141411](https://github.com/user-attachments/assets/05bf9e8b-badf-4866-87b1-6e7b967006bf)
![Screenshot 2025-06-12 141427](https://github.com/user-attachments/assets/642abcfd-dcd8-48f2-9698-2c2037fe1025)


---

## 🙏 Acknowledgements

- [Microsoft Azure AI Internship](https://www.microsoft.com/en-us/azure/)
- [Edunet Foundation](https://www.edunetfoundation.org/)
- The creators of the open-source libraries used in this project.

---

## 📧 Contact

**Jahnavi Sri Harshita Konatala**

- **Email**: [jahnavikonatala21@gmail.com](mailto:jahnavikonatala21@gmail.com)
- **GitHub**: [@jahnavikonatala21](https://github.com/jahnavikonatala21)
