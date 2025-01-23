from collections import namedtuple

# Simplified student record structure
Student = namedtuple("Student", ["name", "id"])

# Persistent storage filename
STUDENTS_FILE = "students.txt"