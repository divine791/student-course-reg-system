class Student:
    def __init__(self, name, matric_number):
        self.name = name
        self.matric_number = matric_number
        self.registered_courses = []

class Course:
    def __init__(self, course_code, course_title):
        self.course_code = course_code
        self.course_title = course_title

class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def register_student(self, student):
        self.students.append(student)

    def register_course(self, student, course):
        student.registered_courses.append(course)

    def display_courses(self):
        print("Available Courses:")
        for course in self.courses:
            print(course.course_code, "-", course.course_title)


# Program Execution
system = RegistrationSystem()

course1 = Course("SEN201", "Software Engineering")
course2 = Course("CSC101", "Introduction to Computer Science")

system.add_course(course1)
system.add_course(course2)

student1 = Student("John Doe", "CU2023/001")
system.register_student(student1)

system.display_courses()
system.register_course(student1, course1)

print("\nRegistered Courses for", student1.name)
for course in student1.registered_courses:
    print(course.course_code, "-", course.course_title)
