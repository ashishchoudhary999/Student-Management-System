from operations import *

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
    