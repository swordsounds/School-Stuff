
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
student_grades = {"John": 88, "Jane": 92, "Molly": 85, "Mary": 90, "Jake": 89}

student_grades.update({"Mike": 0, "Dan": 50})

student_grades["John"] = 22

del student_grades["Mike"]
print(student_grades.pop("Mary"))
print(student_grades.popitem())
print(student_grades)
print(student_grades["Molly"])

def student_loop(student_grades):
    for key, value in student_grades.items():
        print(key, value)
        if value >= 90:
            print(f"{key} has a grade of A or above 90!")
student_loop(student_grades)
def grade_summary(student_grades):
    total_students = len(student_grades)
    highest_grade = max(student_grades.values())
    lowest_grade = min(student_grades.values())
    average_grade = sum(student_grades.values()) / len(student_grades)
    print(f"Total Students: {total_students}")
    print(f"Highest Grade: {highest_grade}")
    print(f"Lowest Grade: {lowest_grade}")
    print(f"Average Grade: {average_grade}")