# 📧 Email Automation Agent

An AI-powered Email Automation System that generates, customizes, and sends emails using an agent-based architecture. This project combines automation, modular design, and a user-friendly Streamlit interface to simplify email communication workflows.

---

## 🌟 Overview

The Email Automation Agent is designed to automate repetitive email-related tasks such as generating email content, selecting appropriate templates, and sending emails through SMTP. The system follows an agent-based architecture where different components collaborate to process requests efficiently.

Whether it's sending welcome emails, internship notifications, reminders, or custom messages, this application streamlines the entire workflow through a simple web interface.

---

## 🚀 Features

### 🤖 Intelligent Email Generation

* Generates professional email content automatically.
* Supports multiple email use cases.
* Reduces manual effort in drafting emails.

### 📩 Automated Email Sending

* Sends emails using SMTP integration.
* Supports dynamic recipients and content.
* Handles end-to-end email workflow.

### 📄 Template-Based Emails

Predefined templates for:

* Welcome Emails
* Reminder Emails
* Internship Emails

### 🧠 Agent-Based Architecture

The application uses specialized agents for:

* Planning tasks
* Executing workflows
* Managing email generation

### 📊 Logging Support

* Tracks application activities.
* Helps in debugging and monitoring.

### 🎨 Interactive User Interface

* Built using Streamlit.
* Simple and easy-to-use dashboard.
* No technical expertise required.

---

## 🏗️ Project Architecture

The system follows a modular architecture:

1. User submits email details through the Streamlit UI.
2. The Email Agent processes the request.
3. Planner creates an execution strategy.
4. Executor performs required actions.
5. Appropriate template is selected.
6. Email content is generated.
7. SMTP service sends the email.
8. Logs are recorded for monitoring.

---

## 📂 Project Structure

```text
email-automation-agent/
│
├── app.py                         # Main application entry point
│
├── agent/                         # Core agent logic
│   ├── email_agent.py
│   ├── planner.py
│   └── executor.py
│
├── config/                        # Configuration settings
│   └── settings.py
│
├── frontend/                      # Streamlit user interface
│   └── ui.py
│
├── tools/                         # Utility modules
│   ├── email_sender.py
│   ├── logger.py
│   ├── test_email.py
│   └── test_smpt.py
│
├── templates/                     # Email templates
│   ├── welcome.txt
│   ├── reminder.txt
│   └── internship.txt
│
├── requirements.txt               # Project dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Ratnanjalikapavarapu28/email-automation-agent.git
cd email-automation-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Option 1

```bash
streamlit run frontend/ui.py
```

### Option 2

```bash
python -m streamlit run frontend/ui.py
```

---

## 📧 Email Workflow

```text
User Input
     │
     ▼
 Email Agent
     │
     ▼
   Planner
     │
     ▼
  Executor
     │
     ▼
 Email Template
     │
     ▼
 SMTP Service
     │
     ▼
 Recipient
```

---

## 🛠️ Technology Stack

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Core Development     |
| Streamlit             | User Interface       |
| SMTP                  | Email Delivery       |
| Agent Architecture    | Workflow Management  |
| Environment Variables | Secure Configuration |

---

## 📌 Future Enhancements

* Gmail API Integration
* Email Scheduling
* Email History Tracking
* Multi-Agent Collaboration
* Dashboard Analytics
* Template Management System
* Cloud Deployment

---

## 🎯 Use Cases

* Automated Welcome Emails
* Internship Offer Notifications
* Reminder Emails
* Internal Team Communication
* Customer Engagement Campaigns
* Bulk Email Automation

---

### Thank You for Visiting This Project! 🚀
