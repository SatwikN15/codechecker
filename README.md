
# 🛡️ CodeGuard

### Automated Code Review and Ticket Management System

---

## 📌 Project Overview

**CodeGuard** is a web-based automated code review system that analyzes source code for errors, warnings, and quality issues using static code analysis techniques.
Whenever an issue is detected, the system **automatically raises a ticket** and displays it on a centralized dashboard for tracking and management.

This project aims to reduce manual code review effort, improve software quality, and provide an efficient issue-tracking mechanism suitable for modern software development environments.

---

## 🎯 Objectives

* Automate source code quality checking
* Detect syntax and logical issues using static analysis
* Automatically generate issue tickets
* Provide a professional dashboard for issue tracking
* Maintain issue records using a database

---

## 🧩 System Architecture

```
User
 │
 │ Web Browser
 ▼
Frontend (HTML + CSS)
 │
 ▼
Flask Backend (Python)
 │
 ├── Code Analysis Engine (Pylint)
 ├── Ticket Management Module
 │
 ▼
SQLite Database
```

---

## 🛠️ Technologies Used

| Component            | Technology  |
| -------------------- | ----------- |
| Programming Language | Python 3.x  |
| Backend Framework    | Flask       |
| Static Code Analysis | Pylint      |
| Frontend             | HTML5, CSS3 |
| Database             | SQLite      |
| Development Tool     | VS Code     |

---

## 📂 Project Structure

```
CodeGuard_Complete_Final_Year/
│
├── app.py                 # Main Flask application
├── code_checker.py        # Code analysis logic
├── ticket_manager.py     # Ticket database operations
├── database.db            # SQLite database (auto-created)
├── sample_code.py         # Sample code for testing
├── requirements.txt       # Project dependencies
│
├── templates/
│   └── dashboard.html     # UI dashboard
│
├── static/
│   └── css/
│       └── style.css      # UI styling
│
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites

* Python **3.9 or above**
* pip package manager

> ⚠️ **Important:**
> Python **3.13** may cause compatibility issues with some packages.
> Recommended: **Python 3.10 / 3.11**

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `pylint` fails:

```bash
pip install --upgrade pip
pip install pylint
```

---

## ▶️ Running the Application

```bash
python app.py
```

Open browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🖥️ Application Workflow

1. User opens the dashboard
2. Clicks **"Run Code Scan"**
3. System analyzes `sample_code.py`
4. Issues are detected using static analysis
5. Tickets are automatically created
6. Tickets appear on the dashboard

---

## 📊 Output Screens

### 🔹 Dashboard

* Displays all raised tickets
* Shows issue description and status
* Professional UI for demonstration

### 🔹 Ticket Status

* OPEN (default)
* Extendable to IN-PROGRESS / CLOSED

---

## 🧪 Sample Input

```python
def add(a, b):
    return a + b

print(add(5))
```

### Sample Output

* Missing function argument
* Code quality warnings
* Ticket raised automatically

---

## 🚀 Future Enhancements

* User authentication and roles
* GitHub repository integration
* Severity classification (Low / Medium / High)
* Email notifications
* Support for Java and JavaScript code
* CI/CD pipeline integration

---

## 📚 Academic Relevance

* Demonstrates **software engineering principles**
* Applies **static code analysis**
* Uses **database-backed issue tracking**
* Suitable for:

  * Final Year Project
  * Mini Project
  * Internship Evaluation
  * GitHub Portfolio

---

## 👨‍💻 Developed By

satwik
Department of Computer Science & Engineering

Just tell me 👍

