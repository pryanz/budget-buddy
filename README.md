# Budget Buddy

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-46E3B7?logo=render&logoColor=white)](https://render.com/)

**Budget Buddy** is a full-stack personal finance application designed to help users track expenses, visualize spending habits, and maintain financial discipline. 

It features secure user authentication, a responsive dashboard, and a containerized architecture for easy deployment.

## Live Demo

**[View the Live Application Here]([https://budget-buddy-demo-pryanz.onrender.com])** *(Note: Hosted on Render Free Tier. Please allow up to 50 seconds for the server to wake up.)*

---

## Key Features

* ** Secure Authentication:** User registration and login system protected with Bcrypt hashing.
* ** Interactive Dashboard:** dynamic overview of total expenses and recent activity.
* ** Expense Tracking:** Create, Read, Update, and Delete (CRUD) expense records.
* ** Responsive Design:** Built with Bootstrap 5 to work seamlessly on mobile and desktop.
* ** Containerized:** Fully Dockerized application ensuring consistency across development and production environments.

---

## Tech Stack

* **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Bcrypt
* **Database:** SQLite (Dev), SQLApi (Compatible)
* **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templating
* **DevOps:** Docker, Docker Compose, Git, Render

---

## Local Setup (Using Docker)

The easiest way to run this application locally is using Docker.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/budget-buddy.git](https://github.com/yourusername/budget-buddy.git)
cd budget-buddy
