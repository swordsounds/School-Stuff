#Dictionary to store students and their grades
students = {"John": 88, "Jane": 92, "Jake": 90, "Molly": "A", "Mary": "B", "Nick": 75}
#Dictionary to store the letter and their associated grade
letters = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 49}
#Main function to call ther other functions to organize things
def main():
    update_dictionary()
    access_elements()
    delete_elements()
    looping_through_dictionary()
    grade_summary()

def update_dictionary():
    print("-----------")
    #Uses the update() method to add and modify the students in the dictionary
    students.update({"Gavin": 100, "Brodie": "A", "John": 100})
    #Print statments to tell the user what has happened
    print("2 Additional students have been added!\n*NEW* Gavin\n*NEW* Brodie")
    print("John now has a grade of 100!")

def access_elements():
    print("-----------")
    #Try and except method to handle errors
    try:
        #Print the grade of mary
        print(f"Mary has a grade of {students.get('Mary')}")
        print(students["Kyle"])
        #Since Kyle is not in the dictionary, raises exception
    except KeyError:
        print(f"Kyle is not in the dictionary!")

def delete_elements():
    print("-----------")
    #Uses del to delete
    del students["Brodie"]
    #Print statement to tell the user what has happened
    print("Deleted Student Brodie, using 'del'")
    #Print statement to tell the user Molly's grade using 'pop'
    print(f"Molly has been removed with a grade of {students.pop('Molly')}, using 'pop'")
    #Assigned the key and value for print statement
    student, grade = students.popitem()
    #
    print(f"{student} has been deleted with a grade of {grade}, using 'popitem'")

def looping_through_dictionary():
    print("-----------")
    #Loop through the dictionary and print out each student's name and their grade
    for student, grade in students.items():
        print(f"{student} has a grade of {grade}")
        #Try and except method to handle ype errors
        try:
            #Condition to see if the student has a number grade greater or equal to 90
            if grade >= 90:
                print(f"{student} has a grade of A or above 90!")
        #Exception if the student has a letter grade is raised
        except TypeError:
            #Gets the letter grades number
            if letters.get(grade) >= 90:
                print(f"{student} has a grade of A or above 90!")

def grade_summary():
    print("-----------")
    #Initialize total score to 0
    total_score = 0 
    #Iterate over students to total up the score
    for student, grade in students.items():
        #Trys the condition to see if the student has a number grade
        try:
            if grade / 1:
                total_score += grade
        #If the student has a letter grade is raises the exception
        except TypeError:
            #Converts letter grade to number
            students[student] = letters.get(grade)
            #Adds letter grade to total score
            total_score += letters.get(grade)
    #Prints the number of students in the dictionary
    print(f"There are {len(students)} students in the dictionary now!") 
    #Prints the highest grade in the dictionary
    print(f"{max(students.values())} was the highest grade!")
    #Prints the lowest grade in the dictionary
    print(f"{min(students.values())} was the lowest grade!")
    #Prints the average grade of the dictionary
    print(f"{round(total_score / len(students), 2)} is the average grade!")

#Runs if ran on the main file
if __name__ == "__main__":
    main()