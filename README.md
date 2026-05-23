# Student Management System API

A backend Student Management System built using FastAPI and SQLite.  
This project provides full CRUD (Create, Read, Update, Delete) operations through REST APIs for managing student records.

---

## Features

- Add Students
- View All Students
- Search Students
- Update Student Details
- Delete Students
- REST API Development
- SQLite Database Integration
- FastAPI Backend
- Interactive Swagger Documentation

---

## Technologies Used

- Python
- FastAPI
- SQLite
- SQL
- Pydantic
- Uvicorn
- Git & GitHub

---

## Project Structure

```bash
Student-Management-System/
│
├── app.py
├── main.py
├── operations.py
├── database.py
├── students.db
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home Route |
| GET | /about | About Route |
| GET | /students | Get All Students |
| POST | /students | Add New Student |
| PUT | /students/{name} | Update Student |
| DELETE | /students/{name} | Delete Student |

---

## How to Run

1. Clone the repository

```bash
git clone <your-repository-link>
```

2. Move into the project folder

```bash
cd Student-Management-System
```

3. Install dependencies

```bash
pip install fastapi uvicorn
```

4. Run FastAPI server

```bash
uvicorn app:app --reload
```

---

## API Documentation

After running the server, open:

```bash
http://127.0.0.1:8000/docs
```

FastAPI automatically provides interactive Swagger API documentation for testing endpoints.

---

## CRUD Operations

| Operation | Description |
|---|---|
| Create | Add new students |
| Read | View/Search students |
| Update | Update existing students |
| Delete | Remove student records |

---

## Learning Outcomes

Through this project, I learned:

- FastAPI fundamentals
- REST API development
- CRUD operations using APIs
- SQLite database integration
- SQL queries
- Pydantic models
- Backend project structure
- Git & GitHub workflow

---

## Future Improvements

- Authentication System (JWT)
- PostgreSQL Integration
- SQLAlchemy ORM
- Better Project Architecture
- Deployment
- Frontend Integration