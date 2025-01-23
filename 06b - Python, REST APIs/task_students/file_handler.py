import os
from schema import Student, STUDENTS_FILE

def load_students():
  """Loads student data from the file."""
  students = []
  if os.path.exists(STUDENTS_FILE):
    try:
      with open(STUDENTS_FILE, "r") as f:
        for line in f:
          name, student_id = line.strip().split(",")
          students.append(Student(name, student_id))
    except FileNotFoundError:
      print(f"Error: File '{STUDENTS_FILE}' not found.")
    except ValueError:
      print(f"Error: Invalid data format in '{STUDENTS_FILE}'.")
  return students

def save_students(students):
  """Saves student data to the file."""
  try:
    with open(STUDENTS_FILE, "w") as f:
      for student in students:
        f.write(f"{student.name},{student.id}\n")
  except Exception as e:
    print(f"Error saving students to file: {e}")
