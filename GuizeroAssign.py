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

def foodWindow():
    window = Window(main_app, title="Food",width=400, height=400, layout="grid")
    food_button = PushButton(main_app, text="Next",grid=[1, 4],padx=100, pady=10, enabled=False)
    drink = CheckBox(window, text="Add Drink",grid=[0, 0])
    food = CheckBox(window, text="Add Food",grid=[0, 1])
    desert = CheckBox(window, text="Add Desert", grid=[0, 2])
    window_button = PushButton(window, text="Next", grid=[1, 4],command=moneyWindow, padx=100, pady=10)


def moneyWindow():
    money_window = Window(window, title="Summary", width=400, height=400, layout="grid")
    payment_options = Combo(money_window, options=["Select", "Cash", "Debit", "Credit"], grid=[0, 0])
    tip_slider = Slider(money_window, start=1, end=5, grid=[0, 1])
    titlebox = TitleBox(money_window, text="asas", grid=[1, 1])
    titlebox = TitleBox(money_window, text="asas", grid=[2, 1])

main_app = App(title="main", width=400, height=400, layout="grid")
window = Window(main_app, visible=False)

text = Text(main_app, text="First Name", grid=[0, 0])
text = Text(main_app, text="Last Name", grid=[0, 1])
text = Text(main_app, text="Grade Level", grid=[0, 2])

f_name = TextBox(main_app, grid=[1, 0])
l_name = TextBox(main_app, grid=[1, 1])
gr_lvl = TextBox(main_app, grid=[1, 2])

food_button = PushButton(main_app, text="Next", grid=[1, 4],command=foodWindow, padx=100, pady=10)




main_app.display()