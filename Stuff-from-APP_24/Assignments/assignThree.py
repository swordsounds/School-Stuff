def main():
    #Created class called Student
    class Student:
        #Initialized with name, age, and student_id attributes
        def __init__(self, name, age, student_id):
            self.name = name
            self.age = age
            self.student_id = student_id
            #Private attribute __gpa, initialized with 0
            self.__gpa = 0
        #Method sets the gpa to new values, checks if it is between 0 and 4.0
        def set_gpa(self, gpa):
            if gpa >= 0.0:
                if gpa > 4.0:
                    print(f"{self.name} has invalid GPA value of {self.__gpa}")
                    self.__gpa = 4.0
                else:
                    self.__gpa = gpa
            else:
                print(f"{self.name} has invalid GPA value of {self.__gpa}")
        #Updates GPA according to studying time
        def study(self, hours):
            self.__gpa += (hours / 10)
            self.set_gpa(self.__gpa)
        #Method to get the students GPA
        def get_gpa(self):
            return self.__gpa
        #Displays the students attributes
        def display_student_info(self):
            print(f"Student {self.name} with ID {self.student_id}"
                  f", age {self.age} has GPA of {self.get_gpa()}")

    #Created three instances of Student object
    s1 = Student("Matt", 17, "000X2f")
    s2 = Student("Nick", 17, "000D6Q")
    s3 = Student("Paul", 17, "000R3R")

    s1.set_gpa(4.0)
    s2.set_gpa(3.0)
    s3.set_gpa(1.0)
    print("---BEFORE STUDYING---")
    s1.display_student_info()
    s2.display_student_info()
    s3.display_student_info()
    print("---------------------")
    s1.study(5)
    s2.study(5)
    s3.study(5)
    print("---AFTER STUDYING---")
    s1.display_student_info()
    s2.display_student_info()
    s3.display_student_info()
    print("--------------------")

#Calls function main if the module is the main module
if __name__ == "__main__":
    main()