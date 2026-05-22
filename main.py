import json
import os
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()

students = []

if os.path.exists("students.txt"):
  with open("students.txt", "r") as file:
    students = json.load(file)

while True: 
 print("1. Add Student")
 print("2. View Students")
 print("3. Search Student")
 print("4. Delete Student")
 print("5. Exit")

 try:
  choice = int(input("Enter your choices: "))
 except ValueError:
   print("Please enter numbers only")
   continue
   
 if choice == 1:
   name = input("Enter name: ")
   age = input("Enter age: ")
   course = input("Enter course: ")

   cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
   )
   conn.commit()

   student = {
     "name": name,
     "age": age,
     "course": course
   }

   students.append(student)

   # Save to file
   with open("students.txt", "w") as file:
     json.dump(students,file)

   print("Students Added Successfully")

 elif choice == 2:
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if len(students) == 0:
      print("No students found")
    else:
      for student in students:
        print(f"Name: {student[1]} | Age: {student[2]} | course: {student[3]}")

 elif choice == 3:
    name = input("Enter student name: ").strip().lower()

    found = False

    for student in students:
        if name in student["name"].strip().lower():
            print("Student Found")
            print(f"Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")
            found = True
    if not found:
        print("Student Not Found")

 elif choice == 4:
   name = input("Enter student name: ")
   found = False
   for student in students:
    if student["name"].strip().lower() == name.strip().lower():
     students.remove(student)
     print("Student Deleted Successfully")
     with open("students.txt", "w") as file:
       json.dump(students, file)
     found = True
     break
   if not found:
       print("Student Not Found")
       
 elif choice == 5:
    print("Exiting...")
    break
 
 else:
    print("Invalid choice")
    