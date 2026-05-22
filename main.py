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

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()

    print("Students Added Successfully")


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if len(students) == 0:
        print("No students found")
    else:
        for student in students:
            print(f"Name: {student[1]} | Age: {student[2]} | course: {student[3]}")


def search_students():
    name = input("Enter student name: ").strip().lower().upper()

    cursor.execute(
      
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    results = cursor.fetchall()

    if len(results) == 0:
        print("Student Not Found")
    else:
        for student in results:
            print("Student Found")
            print(f"Name: {student[1]} | Age: {student[2]} | Course: {student[3]}")


def delete_student():
   name = input("Enter student name: ").strip().lower().upper()

   cursor.execute(
     "DELETE FROM students WHERE name = ?",
     (name,)
   )

   conn.commit()

   if cursor.rowcount > 0:
        print("Student Deleted Successfully")
   else:
       print("Student Not Found")


def update_student():
    old_name = input("Enter student name: ").strip().lower().upper()
    new_name = input("Enter new name: ")
    new_age = input("Enter new age: ")
    new_course = input("Enter new course: ")
    cursor.execute(
        "UPDATE students SET name = ?, age = ?, course = ? WHERE name = ?",
        (new_name, new_age, new_course, old_name)
    )    
    conn.commit()
    if cursor.rowcount > 0:
       print("Student Updated Succesfully")
    else:
       print("Student Not Found")

while True: 
 
 print("1. Add Student")
 print("2. View Students")
 print("3. Search Student")
 print("4. Delete Student")
 print("5. Update Student")
 print("6. Exit")

 try:
  choice = int(input("Enter your choices: "))
 except ValueError:
   print("Please enter numbers only")
   continue
   
 if choice == 1:
    add_student()

 elif choice == 2:
    view_students()
    
 elif choice == 3:
    search_students()

 elif choice == 4:
   delete_student()

 elif choice == 5:
    update_student()
       
 elif choice == 6:
    print("Exiting...")
    break
 
 else:
    print("Invalid choice")
    