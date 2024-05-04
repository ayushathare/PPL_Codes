class Student:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        self.students.append({"name": name, "age": age, "grade": grade})

    def display_students(self):
        for student in self.students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Creating an instance of the Student class
student_manager = Student()

# Adding multiple student entries
student_manager.add_student("Alice", 18, "A")
student_manager.add_student("Bob", 17, "B")
student_manager.add_student("Charlie", 16, "C")

# Displaying all student entries
student_manager.display_students()
