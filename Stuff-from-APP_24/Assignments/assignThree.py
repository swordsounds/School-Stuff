# Instructions:
# Create a Python class called Student with the following attributes:
# 1. name (a string)
# 2. age (an integer)
# 3. student_id (a string)
# 4. __gpa (a private floating-point number, hidden attribute)

# Create an initialization method (__init__) for the Student class to initialize the attributes. The GPA
# should be hidden and set to 0 initially.

# Implement the following methods in the Student class:
# 1. set_gpa(self, gpa): set the GPA for the student. Validate that the GPA is between 0 and 4.0.
# 2. get_gpa(self): A method to get the GPA of the student.
# 3. study(self, hours): accepts hours a student has studied
# updates GPA as follows: GPA += (hours / 10).
# 4. display_student_info(self): display name, age, student ID, and GPA.

# Create three instances of the Student class and demonstrate the functionality of the methods. Initialize
# the attributes and manipulate the GPA using the methods. Display the student information before and
# after studying.
def main():
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
            self.set_gpa(gpa)
        def display_student_info(self):
            return self.name, self.age, self.student_id, self.get_gpa()

    s1 = Student("Matt", 17, "000X2f")
    s2 = Student("Nick", 17, "000D6Q")
    s3 = Student("Paul", 17, "000R3R")

    print(s1.display_student_info())
    print(s2.display_student_info())
    print(s3.display_student_info())

if __name__ == "__main__":
    main()