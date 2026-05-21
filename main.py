import json
import os
students = []

if os.path.exists("students.txt"):
  with open("students.txt", "r") as file:
    students = json.load(file)

while True: 
 print("1. Add Student")
 print("2. View Students")
 print("3. Search Student")
 print("4. Exit")

 try:
  choice = int(input("Enter your choices: "))
 except ValueError:
   print("Please enter numbers only")
   continue
   
 if choice == 1:
   name = input("Enter name: ")
   age = input("Enter age: ")
   course = input("Enter course: ")

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
    if len(students) == 0:
      print("No students found")
    else:
      for student in students:
        print(f"Name: {student['name']} | Age: {student['age']} | course: {student['course']}")

 elif choice == 3:
   name = input("Enter Student name: ")

   found = False

   for student in students:
     if student["name"] == name:
       print("Student Found")
       print(student)
       found = True
       break
     
     if not found:
       print("Student Not Found") 
       
 elif choice == 4:
    print("Exiting...")
    break
 else:
    print("Invalid choice")
    