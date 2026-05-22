from database import conn, cursor

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