from fastapi import FastAPI
from pydantic import BaseModel
from database import conn, cursor


app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str

@app.get("/")
def home():
    return {"message": "FastAPI is working"}

@app.get("/about")
def about():
    return{"message": "This is Student Management API"}

@app.get("/students")
def get_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return {"students": students}


@app.post("/students")
def add_student(student: Student):

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (student.name, student.age, student.course)
    )

    conn.commit()

    return {"message": "Student Added Succesfully"}

@app.delete("/students/{name}")
def delete_student(name: str):
    cursor.execute(
        "DELETE FROM students WHERE name = ?",

        (name,)
    )
    conn.commit()
    if cursor.rowcount > 0:
        return{"message": "Student Deleted Successfully"}

    return {"message": "Student Not Found"}

@app.put("/students/{name}")
def update_student(name: str, student: Student):
    cursor.execute(
        """
        UPDATE students
        SET name = ?, age = ?, course = ?
        WHERE name = ?
        """,
        (student.name, student.age, student.course, name)
    )
    conn.commit()
    if cursor.rowcount > 0:
        return {"message": "Studet Update Succcessfully"}
    
    return {"message": "Student Not Found"}