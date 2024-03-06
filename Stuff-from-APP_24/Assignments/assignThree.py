# Objective: create Student Information System 
#create a class to represent a student, encapsulate its attributes, and implement methods to interact with student data.
# Instructions:
# Create a Python class called Student with the following attributes:
#  name (a string)
#  age (an integer)
#  student_id (a string)
#  __gpa (a private floating-point number, hidden attribute)
# Create an initialization method (__init__) for the Student class to initialize the attributes. The GPA
# should be hidden and set to 0 initially.

# Implement the following methods in the Student class:
#  set_gpa(self, gpa): A method to set the GPA for the student. It should validate that the GPA is
# between 0 and 4.0.
#  get_gpa(self): A method to get the GPA of the student.
#  study(self, hours): A method that accepts the number of hours a student has studied and
# updates the GPA as follows: GPA += (hours / 10).
#  display_student_info(self): A method to display the student's information, including name, age,
# student ID, and GPA.
# Create three instances of the Student class and demonstrate the functionality of the methods. Initialize
# the attributes and manipulate the GPA using the methods. Display the student information before and
# after studying.

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.__gpa = 0
    
    def set_gpa(self, gpa):
        if gpa >= 0 and gpa <= 4.0:
            self.__gpa = gpa
    
    def get_gpa(self):
        return self.__gpa
    def study(self, hours):
        gpa += (hours / 10)
    def display_student_info(self):
        return self.name, self.age, self.student_id, self.get_gpa()

s1 = Student()
s2 = Student()
s3 = Student()

