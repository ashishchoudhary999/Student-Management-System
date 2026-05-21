students = []
while True: 
 print("1. Add Student")
 print("2. View Students")
 print("3. Exit")

 choice = int(input("Enter your choices: "))

 if choice == 1:
   student = input("Enter student name: ")
   students.append(student)
   print("Students Added Successfully")
 elif choice == 2:
    for student in students:
      print(student)    
 elif choice == 3:
    print("Exiting...")
    break
 else:
    print("Invalid choice")
    