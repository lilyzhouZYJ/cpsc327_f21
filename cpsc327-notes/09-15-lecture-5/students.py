from courses import Department
from comparable import ComparableMixin

class Person(ComparableMixin):
    def __init__(self, name, surname, number, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        super().__init__(*args, **kwargs)

    def __lt__(self, other):
        return self.number < other.number

class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = ("undergrad", "postgrad")

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enroll(self, course):
        self.classes.append(course)

class StaffMember(Person):
    PERMANENT, TEMPORARY = ("permanent", "temporary")

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)

# multiple inheritance!
class ULA(Lecturer, Student):
    def __init__(self, *args, **kwargs):
        super(ULA, self).__init__(*args, **kwargs)


if __name__ == "__main__":

    cs_dept = Department("Computer Science", "CPSC")
    oop = cs_dept.add_course("Object-oriented programming", "CPSC327", 1)
    oop_2021 = oop.add_running(2021)

    tim = Lecturer(StaffMember.PERMANENT, "Tim", "Barron", "123456789")
    tim.assign_teaching(oop_2021)

    jane = Student(Student.POSTGRADUATE, "Jane", "Smith", "SMTJNX045")
    jane.enroll(oop_2021)

    kelly = ULA(StaffMember.TEMPORARY, Student.UNDERGRADUATE, "Kelly", "Rudder", "1")
    kelly.assign_teaching(oop_2021)
    print(kelly.student_type)
    print(kelly.employment_type)

    print(ULA.__mro__)  # see the MRO of ULA class
    # MRO: ULA, Lecturer, StaffMember, Student, Person, ComparableMixin, object
