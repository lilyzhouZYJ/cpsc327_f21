from courses import Department

# Example of how we can achieve inheritance (and
# multiple inheritance) with composition.

class Learner:
    def __init__(self):
        self.classes = []

    def enroll(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        # mark whether an instance is learner, teacher, or both (i.e. ULA)
        self.learner = learner
        self.teacher = teacher

    def enroll(self, course):
        if not hasattr(self, "learner"):
            raise NotImplementedError()

        self.learner.enroll(course)

    def assign_teaching(self, course):
        if not hasattr(self, "teacher"):
            raise NotImplementedError()

        self.teacher.assign_teaching(course)



cs_dept = Department("Computer Science", "CPSC")
oop = cs_dept.add_course("Object-oriented programming", "CPSC327", 1)
oop_2020 = oop.add_running(2020)

intro = cs_dept.add_course("Intro to computer science", "CPSC201", 1)
intro_2020 = intro.add_running(2020)

# create jane as ULR (both Learner and Teacher)
jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.learner.enroll(oop_2020)
jane.teacher.assign_teaching(intro_2020)

# create tim as teacher
# note that we need keyword argument;
# otherwise it will plug Teacher() into learner attribute
tim = Person("Tim", "Barron", "SMTJNX045", teacher=Teacher())
tim.assign_teaching(oop_2020)