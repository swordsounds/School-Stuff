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




students = {"John": 88, "Jane": 92, "Jake": 90, "Molly": "A", "Mary": "B"}

letters = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 49}
def main():
    update_dictionary()
    access_elements()
    delete_elements()
    looping_through_dictionary()
    grade_summary()


def student_display():
        for student, grade in students.items():
            print(student, grade)

def update_dictionary():
    print("-----------")
    students.update({"Gavin": 100, "Brodie": "A", "John": 100})
    print("2 Additional students have been added!\n*NEW* Gavin\n*NEW* Brodie")
    print("John now has a grade of 100!")

def access_elements():
    print("-----------")
    try:
        print(students["John"])
        print(students["Kyle"])
    except KeyError:
        print(f"Kyle is not in the dictionary!")

def delete_elements():
    print("-----------")
    del students["Brodie"]
    print("Deleted Student Brodie, using 'del'")
    print(f"Molly has been removed with a grade of {students.pop('Molly')}, using 'pop'")
    print(f"{students.popitem()} has been deleted, using 'popitem'")

def looping_through_dictionary():
    print("-----------")
    for student, grade in students.items():
        try:
            if grade >= 90:
                print(f"{student} has a grade of A or above 90!")
        except TypeError:
            if letters.get(grade) >= 90:
                print(f"{student} has a grade of A or above 90!")

def grade_summary():
    print("-----------")
    total_score = 0

    for student, grade in students.items():
        try:
            if grade / 1:
                total_score += grade
        except TypeError:
            students[student] = letters.get(grade)
            total_score += letters.get(grade)


    print(total_score) 
    print(len(students))
    print(max(students.values()))
    print(min(students.values()))
    print(round(total_score / len(students), 2))


if __name__ == "__main__":
    main()