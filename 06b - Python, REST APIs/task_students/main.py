import os
from schema import STUDENTS_FILE

from student_operations import (
    add_student,
    view_students,
    update_student,
    delete_student,
)

def main_menu():
  """Displays the main menu options."""
  print("\nStudent Management System")
  print("1. Add Student")
  print("2. View Students")
  print("3. Update Student")
  print("4. Delete Student")
  print("5. Exit")

def main():
  """Main function to handle user interaction."""
  while True:
    main_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
      name = input("Enter student name: ")
      student_id = input("Enter student ID: ")
      add_student(name, student_id)
    elif choice == "2":
      view_students()
    elif choice == "3":
      student_id = input("Enter student ID to update: ")
      updated_name = input("Enter new student name: ")
      update_student(student_id, updated_name)
    elif choice == "4":
      student_id = input("Enter student ID to delete: ")
      delete_student(student_id)
    elif choice == "5":
      print("Exiting Student Management System...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")

# Check if the student data file exists. If not, create it.
if not os.path.exists(STUDENTS_FILE):
  open(STUDENTS_FILE, 'w').close()
main()