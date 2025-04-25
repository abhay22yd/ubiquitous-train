# AI-Powered Phishing & Threat Intelligence Detection System 🚨🛡️

An intelligent cybersecurity solution that uses Machine Learning and AI to detect phishing attacks in real time, leveraging threat intelligence APIs and NLP-based classification models. Designed to mitigate social engineering risks across emails, URLs, and short messages.

---

## 🔍 Problem Statement

Phishing remains one of the most prevalent cyber threats worldwide. It targets individuals and organizations via deceptive emails, malicious links, and SMS messages to steal sensitive information. Traditional spam filters and blacklists are reactive and ineffective against zero-day phishing tactics. This project aims to develop a proactive, AI-driven detection system that flags phishing attempts with high accuracy and minimal latency.

---

## 🎯 Objectives

- Detect phishing attempts in:
  - Emails (subject, body, sender)
  - URLs (reputation, structure, redirect behavior)
  - SMS/text messages
- Use NLP and AI models for classification
- Integrate public threat intelligence APIs (e.g., VirusTotal, AbuseIPDB)
- Provide real-time inference via RESTful API
- Visualize threats and logs via a dashboard
- Add a browser extension for live detection (Stretch Goal)

---

## 🧱 Features

- AI/ML-powered phishing detection (emails, URLs, messages)
- Real-time backend API with JSON responses
- Threat enrichment via intelligence APIs
- Admin dashboard for analytics and monitoring
- Secure data handling and logging
- Stretch Goals (in progress): Browser extension, Feedback loop

---

## 🧠 Tech Stack

- Programming: Python  
- ML/NLP: Scikit-learn, BERT, HuggingFace Transformers  
- Data: Pandas, NLTK, PhishTank, VirusTotal API  
- Backend API: FastAPI / Flask  
- Dashboard: React.js / Streamlit  
- Database: SQLite / PostgreSQL  
- DevOps: Git, Docker (optional), Postman  

---

## 🧩 System Architecture

1. Data Collection (PhishTank, scraped examples)  
2. Preprocessing & Feature Engineering (NLP-based)  
3. Model Training (ML & Deep Learning Models)  
4. Inference API (FastAPI or Flask)  
5. Threat Intelligence Lookup (VirusTotal, AbuseIPDB)  
6. Logging, Alerting, and Visualization  

---

## 🚀 Getting Started

1. Clone the Repository:
    ```bash
    git clone https://github.com/your-username/phishing-threat-intel-system.git
    cd phishing-threat-intel-system
    ```

2. Create and Activate a Virtual Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Application:
    ```bash
    python app.py  # or use uvicorn if using FastAPI
    ```

5. Access Dashboard:
    Open http://localhost:8000 or as specified in the dashboard directory

---

## 📊 Example API Request

POST /predict

```json
{
  "email_subject": "Urgent: Your Account is Suspended",
  "email_body": "Click here to verify your account...",
  "url": "http://suspicious-link.com"
}
