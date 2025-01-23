from file_handler import load_students, save_students
from schema import Student

def add_student(name, student_id):
  """Adds a new student record."""
  students = load_students()
  new_student = Student(name, student_id)
  students.append(new_student)
  save_students(students)
  print(f"Student {name} (ID: {student_id}) added successfully!")

def view_students():
  """Prints a list of all students."""
  students = load_students()
  if not students:
    print("No students found.")
    return

  print("Registered Students:")
  for student in students:
    print(f"- Name: {student.name}, ID: {student.id}")

def update_student(student_id, updated_name):
  """Updates the name of a student."""
  students = load_students()
  for i, student in enumerate(students):
    if student.id == student_id:
      students[i] = students[i]._replace(name=updated_name)
      save_students(students)  # Save after update
      print(f"Student ID {student_id} name updated to {updated_name}.")
      return

  print(f"Student with ID {student_id} not found.")

def delete_student(student_id):
  """Deletes a student record."""
  students = load_students()
  for i, student in enumerate(students):
    if student.id == student_id:
      del students[i]
      save_students(students)
      print(f"Student ID {student_id} deleted successfully.")
      return

  print(f"Student with ID {student_id} not found.")

# Example Usage (You'd typically put this in main.py)
if __name__ == "__main__":
  add_student("Alice", "123")
  add_student("Bob", "456")
  view_students()
  update_student("123", "Alicia")
  view_students()
  delete_student("456")
  view_students()