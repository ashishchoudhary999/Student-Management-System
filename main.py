students = []
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
   print("Students Added Successfully")
 elif choice == 2:
    for student in students:
      print(student)    
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
    