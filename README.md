# 📧 Email Automation Agent

An AI-powered Email Automation system that generates and sends smart emails using an agent-based architecture. Built using Python and Streamlit.

---

## 🚀 Features

- 🧠 AI-based email generation using agent workflow
- 📩 Automated email sending using SMTP
- 🧾 Predefined email templates (welcome, reminder, internship)
- ⚙️ Planner + Executor agent architecture
- 📊 Logging system for tracking execution
- 🎨 Simple Streamlit web interface

---

## 🏗️ Project Structure

email-automation-agent/
│
├── app.py                  # Main entry (Streamlit)
│
├── core/                   # AI logic (IMPORTANT PART)
│   ├── planner.py
│   ├── executor.py
│   └── email_agent.py
│
├── utils/                  # Helper functions
│   ├── email_sender.py
│   ├── logger.py
│
├── config/                 # Settings
│   └── settings.py
│
├── frontend/               # UI layer
│   └── ui.py
│
├── templates/              # Email templates
│   ├── welcome.txt
│   ├── reminder.txt
│   └── internship.txt
│
├── tests/                  # Test files (rename tools → tests)
│   ├── test_email.py
│   └── test_smtp.py
│
├── .env                    # ignored
├── .gitignore
├── requirements.txt
└── README.md

## ⚙️ Installation

git clone https://github.com/Ratnanjalikapavarapu28/email-automation-agent.git  
cd email-automation-agent  
pip install -r requirements.txt  

---

## ▶️ Run the Application

Option 1 (Recommended)

streamlit run frontend/ui.py  

Option 2

python -m streamlit run frontend/ui.py  

---

## 📧 How It Works

1. User enters email request in Streamlit UI  
2. Planner agent breaks request into steps  
3. Executor agent processes each step  
4. Email is generated using templates  
5. Email is sent via SMTP tool  
6. Logs are stored for tracking  

---

## 🧠 Tech Stack

- Python 🐍  
- Streamlit 🎨  
- SMTP Email Service 📩  
- Modular Agent Architecture  

---

## 📌 Future Improvements

- Gmail API integration  
- Email scheduling system  
- Database for email history  
- Multi-agent collaboration  
- Better UI dashboard  

---

## ⚠️ Important Note

Create a `.env` file for sensitive credentials like:  
- Email username  
- Email password / app password  

Do NOT upload `.env` to GitHub.

---
