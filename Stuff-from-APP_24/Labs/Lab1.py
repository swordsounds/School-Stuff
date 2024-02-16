# 2. Update Dictionary:
# • Add two more students with their grades.
# • Modify the grade of one student.

# 3. Accessing Elements:
# • Print the grade of a specific student.
# • Try accessing the grade of a student not in the dictionary and handle the potential
# KeyError using a try-except block.

# 4. Delete Elements:
# • Use the del keyword to remove a student from the dictionary.
# • Use the pop() method to remove another student and print the removed grade.
# • Use the popitem() method and display the removed item.

# 5. Looping Through the Dictionary:
# • Write a loop to print out each student's name and their grade.
# • Modify the loop to print the names of students who have a grade of "A" or above 90.

# 6. Bonus Challenge:
# • Create a function grade_summary that takes a dictionary of student grades and prints a
# summary: the total number of students, the highest grade, the lowest grade, and the
# average grade.


letters = {"A": 90, "B": 80, 
           "C": 70, "D": 60, 
           "F": 0}

student_grades = {"JOHN": 88, 
                  "JANE": 92, 
                  "MOLLY": "A", 
                  "MARY": "B",
                 "JAKE": 89}
def menu():
    print("")
    print("1. Update Dictionary")
    print("2. Accessing Elements")
    print("3. Delete Elements")
    print("4. Loop throught the Dictionary")
    print("5: View Items of the Dictionary")
    print("Exit to exit")
    print()

def main():
    while True:
        try:
            menu()

            user_input = input("What would you like to do?: ")
            print()
            if user_input == "1":
                for key in student_grades.keys():
                    print(key)
                print()
                input_student = input("Modify a student's grade: ")
                input_grade_change = int(input("What grade would you like to change it to?: "))
                update_student(student_grades, input_student.upper(), input_grade_change)
            elif user_input == "2":
                input_student = input("What student would you like to access?: ")
                view_grade(student_grades, input_student.upper())
            elif user_input == "3":
                delete_student(student_grades)
            elif user_input == "4":
                pass
            elif user_input == "5":
                for key, value in student_grades.items():
                    print(key, "," ,value)
            else:
                quit()
        except Exception:
            print("Please enter a valid input!")

def update_student(student_grades, input_student, input_grade_change):
    student_grades.update({input_student: input_grade_change})
    print("Grade has been updated!")
    student_grades.update({"BRODIE": "A", "GAVIN": "A"})
    print("2 Additional students have been added!")

def view_grade(student_grades, input_student):
    try:
        print(f"{input_student}'s grade is {student_grades[input_student]}")
    except KeyError:
        print(f"{input_student} is not in the dictionary!")

def delete_student(student_grades):
    del student_grades["MARY"]
    print("Deleted Student MARY, using 'del'")
    print(f"{student_grades.pop('BRODIE')} has been deleted")
    print(f"{student_grades.popitem()} has been deleted")

def good_grades(student_grades):
    for key in student_grades.keys():
        try:
            if student_grades[key] >= 90:
                print(f"{key} has a grade of A or above 90!")
        except Exception:
            if letters.get(student_grades.get(key)) >= 90:
                print(f"{key} has a grade of A or above 90!")
   

def total_grades(student_grades):
    global grade_summary
    grade_summary = 0
    for value in student_grades.values():
        try:
            if value / 1:
                grade_summary += value 
        except TypeError:
            grade_summary += letters.get(value)

if __name__ == "__main__":
    main()