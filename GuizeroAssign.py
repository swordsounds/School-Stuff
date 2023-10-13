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

def info_window():
    text_info = Text(information, f_name.value)
    text_info = Text(information, l_name.value)
    text_info = Text(information, gr_lvl.value)
    main_app.hide()
    information.show()

def options_window():
    information.hide()
    options.show()
    
def optional_window():
    options.hide()
    optional.show()

def payment_window():
    optional.hide()
    payment.show()

def summary_window():
    if choice_lunch.value == "Bread":
        add_cost_primary = 30
        loaf.show()
    elif choice_lunch.value == "Toast":
        add_cost_primary = 80
        piece_toast.show()
    elif choice_lunch.value == "French Toast":
        add_cost_primary = 2
        piece_french_toast.show()
    else:
        add_cost_sndry = 0
        text = Text(summary, "None Selected")
    if choice_sndry.value == "Dessert":
        add_cost_sndry = 5
        dessert.show()
    elif choice_sndry.value == "Drink":
        add_cost_sndry = 7
        drink.show()
    elif choice_sndry.value == "Condements":
        add_cost_sndry= 20
        ketchup.show()
    else:
        add_cost_sndry = 0
        text = Text(summary, "None Selected")
    pay_method = Text(summary, text=f"Payment Method: {payment_optns.value}")
    total = Text(summary, text=f"Total: {int(slider.value) + add_cost_sndry + add_cost_primary}")
    text_choice_lunch = Text(summary, choice_lunch.value)
    text_choice_sndry = Text(summary, choice_sndry.value)
    payment.hide()
    summary.show()


main_app = App(title="main", width=400, height=400, layout="grid")
text_FN = Text(main_app, text="First Name", grid=[0, 0])
text_LN = Text(main_app, text="Last Name", grid=[0, 1])
text_GR = Text(main_app, text="Grade Level", grid=[0, 2])
text = Text(main_app, grid=[0, 6])
f_name = TextBox(main_app, grid=[1, 0])
l_name = TextBox(main_app, grid=[1, 1])
gr_lvl = TextBox(main_app, grid=[1, 2])
next_btn = PushButton(main_app, text="Next", grid=[1, 4],command=info_window, padx=100, pady=10)

# Info window
information = Window(main_app, title="Information", width=400, height=400, visible=False)
next_btn = PushButton(information, text="Next", padx=100, pady=10, command=options_window)

# Lunch Options window
options = Window(main_app, title="Options",width=400, height=400,visible=False)
choice_lunch = ButtonGroup(options, options=["None","Bread", "Toast", "French Toast"], selected="None")
next_btn = PushButton(options, text="Next", padx=100, pady=10, command=optional_window)

# Optional options window
optional = Window(main_app, title="Optional",width=400, height=400,visible=False)
choice_sndry = ButtonGroup(optional, options=["None", "Drink", "Dessert", "Condements"], selected="None")
next_btn = PushButton(optional, text="Next", padx=100, pady=10, command=payment_window)

# Payment window
payment = Window(main_app, title="Payment",width=400, height=400,visible=False)
slider = Slider(payment, start=1, end=5, grid=[0,5])
payment_optns = Combo(payment, options=["None Selected", "Credit", "Debit", "Cash"], selected="None Selected")
next_btn = PushButton(payment, text="Next", padx=100, pady=10, command=summary_window)

#Summary window
summary = Window(main_app, title="Summary", width=400, height=400,visible=False)


dessert = Picture(summary, image="assets\dessert.png", width=100, height=100, visible=False)
drink = Picture(summary, image="assets\drink.png", width=100, height=100, visible=False)
ketchup = Picture(summary, image="assets\ketchup.png", width=100, height=100, visible=False)
loaf = Picture(summary, image="assets\loaf.png", width=100, height=100, visible=False)
piece_toast = Picture(summary, image="assets\piece_toast.png", width=100, height=100, visible=False)
piece_french_toast = Picture(summary, image="assets\piece_french_toast.png", width=100, height=100, visible=False)



main_app.display()