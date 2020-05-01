#class definition
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

#object initialization
from classes_and_objects import Student
student1 = Student("Jim Carrew", "Business", 3.5, False)
student2 = Student("Pamela Smith", "IT", 4.5, False)
print(student1)
print(student2)