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

def counter(imacry, x):
         imacry.value = int(x)

def food_window():
    window = Window(main_app, title="New Window",width=400, height=400,visible=True)
    text_info = Text(window, f_name.value)
    text_info = Text(window, l_name.value)
    text_info = Text(window, gr_lvl.value)
    choice = ButtonGroup(window, options=["Drink", "Desert", "Food"], selected="None")
    next_btn = PushButton(window, text="Next", padx=100, pady=10, command=payment_window)

def payment_window():
    window = Window(main_app, title="Summary",width=400, height=400,visible=True)
    slider = Slider(window, start=1, end=5, grid=[0,5])
    payment_optns = Combo(window, options=["None Selected", "Credit", "Debit", "Cash"], selected="None Selected")
    picture = Picture(window, image="guizero.png")


main_app = App(title="main", width=400, height=400, layout="grid")



text_FN = Text(main_app, text="First Name", grid=[0, 0])
text_LN = Text(main_app, text="Last Name", grid=[0, 1])
text_GR = Text(main_app, text="Grade Level", grid=[0, 2])
text = Text(main_app, grid=[0, 6])

f_name = TextBox(main_app, grid=[1, 0])
l_name = TextBox(main_app, grid=[1, 1])
gr_lvl = TextBox(main_app, grid=[1, 2])

food_button = PushButton(main_app, text="Next", grid=[1, 4],command=food_window, padx=100, pady=10)






main_app.display()