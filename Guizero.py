# Allows the user to complete a fillable form (TextBox) seeking the following information - First Name, Last Name, and Their Grade Level
# This information must then be displayed in a new Window - the new Window must have a PushButton that closes the new info summary Window
# A ButtonGroup should be displayed that gives the user the opportunity to select 1 of 3 lunch options
# A 'next' PushButton should be used to forward the user to the 'optional items' menu in a new Window.
# This 'optional items menu needs to be the form of a CheckBox, and it should contain at least 3 items (Drink, Desert, etc,)
# Another 'next' PushButton should be used to forward the user to the 'pay options' menu in a new Window (Cash, Debit, Credit) -

# This menu should be in the form of a Combo Widget
# The program must have a Slider Widget that allows the user to select a tip between $1 and $5.
# The payment option they select should result in an appropriate text response that communicates the total that they owe.
# When you user has completed the entire GUI form, a picture should display, showing their food choice, and the total cost of their meal.

from guizero import *
arr = []
def main():
    the_main_app = App(title="The Assign", width=1000, height=1000)
    first_name = TextBox(the_main_app, text="Enter First Name:", width=25, height=2)
    last_name = TextBox(the_main_app, text="Enter Last Name:", width=25, height=2)
    grade_level = TextBox(the_main_app, text="Enter grade Level:", width=25, height=2)

    the_main_app.display()
    print(arr)



if __name__ == '__main__':
    main()