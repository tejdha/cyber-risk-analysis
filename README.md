# 🛡️ Cyber Risk Analysis – Backend API

A Django-powered backend for analyzing and managing cybersecurity threats. This RESTful API serves structured log data for frontend dashboards, enabling real-time visibility into login failures, threat severity, and system events.

---

## 🚀 Features

- 🔐 Secure API endpoints for log retrieval
- 📊 Structured data for frontend analytics cards
- 🧠 Severity-based filtering and timestamped events
- 🌐 CORS-enabled for frontend integration
- ⚙️ Modular Django architecture for scalability

---

## 📦 Tech Stack

- **Backend**: Django + Django REST Framework  
- **Database**: SQLite (dev) / PostgreSQL (prod-ready)  
- **API Format**: JSON  
- **Deployment Ready**: Render / Railway / Fly.io

---

## 📁 Folder Structure
cyber-risk-analysis/
├── manage.py 
├── backend/ 
│  ├── models.py
│  ├── views.py
│  ├── urls.py 
│  └── serializers.py
├── requirements.txt
├── Procfile
└── README.md



---

## 🔗 API Endpoints

| Endpoint                | Method | Description                     |
|------------------------|--------|---------------------------------|
| `/api/logs/`           | GET    | Fetch all system logs           |
| `/api/login-failures/` | GET    | Retrieve failed login attempts  |
| `/api/threats/`        | GET    | Get threat-level summaries      |

---

## 🧪 Local Setup

```bash
git clone https://github.com/tejdha/cyber-risk-analysis.git
cd cyber-risk-analysis
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver


👨‍💻 Author
Prabhas Mallepogu
 MBA + B.Tech | Fullstack Developer
 Focused on scalable, secure, user-first platforms
