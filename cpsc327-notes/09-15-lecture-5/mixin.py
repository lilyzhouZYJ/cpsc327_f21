from courses import Department

from students import Person


class LearnerMixin():
    def __init__(self, *args, **kwargs):
        print("learnermixin init")
        self.classes = []
        super().__init__(*args, **kwargs)


    def enroll(self, course):
        self.classes.append(course)


class TeacherMixin():
    "This is a mixin that adds courses taught to other Person objects"
    def __init__(self, *args, **kwargs):
        print("TeacherMixin init")
        self.courses_taught = []
        super().__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class ULA(Person, LearnerMixin, TeacherMixin):
    # just bringing in functionality from the two mixins

    def __init__(self, *args, **kwargs):
        # initializer from Person
        super(Person, self).__init__(*args, **kwargs)

if __name__ == "__main__":


    print(ULA.__mro__)

    cs_dept = Department("Computer Science", "CPSC")
    oop = cs_dept.add_course("Object-oriented programming", "CPSC327", 1)
    oop_2021 = oop.add_running(2021)

    intro = cs_dept.add_course("Intro to computer science", "CPSC201", 1)
    intro_2021 = intro.add_running(2021)

    jane = ULA("Jane", "Smith", "SMTJNX045")

    jane.enroll(oop_2021)
    jane.assign_teaching(intro_2021)

    print(jane.classes)


