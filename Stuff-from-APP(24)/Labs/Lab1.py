
# Requirements:
# • Python installed on your computer or access to an online Python interpreter.
# • Basic knowledge of Python syntax.
# Instructions:
# 1. Create a Dictionary:
# • Create a dictionary named student_grades with at least five student names (as keys)
# and their corresponding grades (as values). Use a mix of letter grades (e.g., "A", "B") and
# numeric grades (e.g., 88, 92).
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
           "E": 50, "F": 0}

def main():
    student_grades = {"John": 88, "Jane": 92, "Molly": "A", "Mary": "B", "Jake": 89}
    updated_dict(student_grades)
    delete_student(student_grades)
    good_grades(student_grades)
    grade_summary(student_grades)
    print(student_grades)

def letter_grades(x):
    for key in letters.keys():
        if letters[key] == x:
            letters[key] += grade_summary()

def updated_dict(student_grades):
    student_grades.update({"John": 90, "Dan": 89})

def delete_student(student_grades):
    del student_grades["John"]
def good_grades(student_grades):
    for key in student_grades.keys():
        try:
            if student_grades[key] >= 90:
                print(f"{key} has a grade of A or above 90!")
        except TypeError:
            letter_grades(student_grades(key))

def grade_summary(student_grades):
    try:
        total_students = len(student_grades)
        highest_grade = max(student_grades.values())
        lowest_grade = min(student_grades.values())
        average_grade = sum(student_grades.values()) / len(student_grades)
        print(f"Total Students: {total_students}")
        print(f"Highest Grade: {highest_grade}")
        print(f"Lowest Grade: {lowest_grade}")
        print(f"Average Grade: {average_grade}")
    except TypeError:
        print("Idk")

if __name__ == "__main__":
    main()