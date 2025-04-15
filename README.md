# 📦 Mboa-Test2 – Simple Flask App with SQLite & Docker

Hey there 👋! Welcome to **Mboa-Test2**, my humble Flask + Docker project made with passion, lots of Googling 🧠, and a bit of stubbornness.

---

## 🚀 Project Overview

This is a beginner-friendly Flask application that connects to a local SQLite database. It's containerized with Docker and ready to be deployed using Docker Compose.

The goal of this project is to:

- ✅ Understand how to use Flask with SQLAlchemy (ORM)
- ✅ Learn how to containerize a Python app
- ✅ Explore database management using SQLite
- ✅ Practice version control and collaboration using Git & GitHub
- ✅ Laugh a little at the bugs I met along the way 😅

---

## 🛠 Technologies Used

- **Python 3.11** 🐍
- **Flask** – lightweight web framework
- **Flask-SQLAlchemy** – ORM for database handling
- **SQLite** – local database for simplicity
- **Docker** – containerization
- **Docker Compose** – multi-container setup
- **Git & GitHub** – version control and collaboration

---

## 🧪 How to Run the App Locally

### 1. Clone the Repo

git clone https://github.com/AlbanE237/mboa-test2.git
cd mboa-test2

Build and Run with Docker Compose

docker-compose up --build

Access the app at http://localhost:5000

Initialize the Database

Once the app is running, open your browser and go to:

http://localhost:5000/init-db
You should see: "Database initialized!"

Project Structure

mboa-test2/
│
├── app.py                  # Main Flask app
├── Dockerfile              # Docker instructions
├── docker-compose.yml      # Compose config
├── models.py               # SQLAlchemy DB models
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files
├── .dockerignore           # Docker ignore file
└── README.md               # You're here!

Project Status
🚧 Still under development
I'm planning to add:

✨ Basic CRUD operations (Create, Read, Update, Delete)

🧪 Unit tests

🐳 CI/CD with GitHub Actions

🔐 Security improvements

📊 Monitoring and logging

🤝 Contributing
I'm learning — but you're welcome to fork the repo, suggest improvements, or just leave a star ⭐.

## 📬 Contact

**👤 Name**: Alban Eboua  
**🔗 LinkedIn**: [linkedin.com/in/albaneboua](https://www.linkedin.com/in/albaneboua/)  
**💻 GitHub**: [github.com/AlbanE237](https://github.com/AlbanE237)


🧠 Final Words
Mistakes were made.
Containers were rebuilt.
Debugging happened.
But hey, that's DevOps life, right? 😂
