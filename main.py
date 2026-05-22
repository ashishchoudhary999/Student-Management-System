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

 elif choice == 4:
   name = input("Enter student name: ")
   cursor.execute(
     "DELETE FROM students WHERE name = ?",
     (name,)
   )
   conn.commit()
   if cursor.rowcount > 0:
        print("succes")
   else:
     print(" not found")
  
       
 elif choice == 5:
    print("Exiting...")
    break
 
 else:
    print("Invalid choice")
    