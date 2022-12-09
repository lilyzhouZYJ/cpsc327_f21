class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.classes = []       # Student aggregates CourseRunning

    def enroll(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)


class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, description, course_code, credits):
        self.courses[course_code] = Course(description, course_code, credits, self)
        return self.courses[course_code]


class Course:
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department

        self.runnings = []

    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]


class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []  # CourseRunning aggregates Student

    def add_student(self, student):
        self.students.append(student)

    def __repr__(self):
        return f"{self.course.course_code} {self.year}"




maths_dept = Department("Mathematics and Applied Mathematics", "MAM")
mam1000w = maths_dept.add_course("Mathematics 1000", "MAM1000W", 1)
mam1000w_2021 = CourseRunning(mam1000w, "2021")
mam1000w.add_running(mam1000w_2021)


bob = Student("Bob", "Smith")
bob.enroll(mam1000w_2021)

print(bob.classes)

repr(bob)