class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        student_id = input("Enter Student ID: ")
        course = input("Enter Course: ")
        student = Student(name, age, student_id, course)
        self.students.append(student)
        print("Student Added Successfully\n")

    def display_students(self):
        if not self.students:
            print("No students available.\n")
            return
        for s in self.students:
            print(f"Name: {s.name}, Age: {s.age}, ID: {s.student_id}, Course: {s.course}")
        print()

    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        for s in self.students:
            if s.student_id == student_id:
                print(f"Name: {s.name}, Age: {s.age}, ID: {s.student_id}, Course: {s.course}\n")
                return
        print("Student not found\n")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Student Deleted Successfully\n")
                return
        print("Student not found\n")


system = StudentManagementSystem()

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.display_students()
    elif choice == "3":
        system.search_student()
    elif choice == "4":
        system.delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")
