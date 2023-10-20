from guizero import *

def info_window():
    text_info = Text(information, f"First Name: {f_name.value}")
    text_info = Text(information, f"Last Name: {l_name.value}")
    text_info = Text(information, f" Grade Level: {gr_lvl.value}")
    next_btn = PushButton(information, text="Next", padx=100, pady=10, command=options_window)
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

def close_window():
    summary.hide()
def add_optional():
    choice_scndary = 1
def summary_window():
    add_cost_sndry = 0
    text_final = []
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
        add_cost_primary = 0

    if check_Drink.value == 1:
        add_cost_sndry += 2
        text_final.append("Drink") 
    if check_Dessert.value == 1:
        add_cost_sndry += 5
        text_final.append("Dessert") 
    if check_Condements.value == 1:
        add_cost_sndry += 10
        text_final.append("Condements") 

    pay_method = Text(summary, text=f"Payment Method: {payment_optns.value}")
    total = Text(summary, text=f"Total: ${int(slider.value) + add_cost_sndry + add_cost_primary}")
    text_choice_lunch = Text(summary, f"Main Dish: {choice_lunch.value}")
    text_choice_sndry = Text(summary, f"Optional Dish(s): {' '.join(text_final)}")
    next_btn = PushButton(summary, text="Close", grid=[1, 4],command=close_window, padx=100, pady=10)
    payment.hide()
    summary.show()


main_app = App(title="Info", width=400, height=400, layout="grid")
text_FN = Text(main_app, text="First Name:", grid=[0, 0])
text_LN = Text(main_app, text="Last Name:", grid=[0, 1])
text_GR = Text(main_app, text="Grade Level:", grid=[0, 2])
text = Text(main_app, grid=[0, 6])
f_name = TextBox(main_app, grid=[1, 0])
l_name = TextBox(main_app, grid=[1, 1])
gr_lvl = TextBox(main_app, grid=[1, 2])
next_btn = PushButton(main_app, text="Next", grid=[1, 4],command=info_window, padx=100, pady=10)

# Info window
information = Window(main_app, title="Info Summary", width=400, height=400, visible=False)


# Lunch Options window
options = Window(main_app, title="Options",width=400, height=400,visible=False)
choice_lunch = ButtonGroup(options, options=["None Selected","Bread", "Toast", "French Toast"], selected="None Selected")
next_btn = PushButton(options, text="Next", padx=100, pady=10, command=optional_window)

# Optional options window
optional = Window(main_app, title="Optional",width=400, height=400,visible=False)
check_None = CheckBox(optional, text="None Selected", grid=[1, 5])
check_Drink = CheckBox(optional, text="Drink", grid=[1, 6], command=lambda: drink.show())
check_Dessert = CheckBox(optional, text="Dessert", grid=[1, 7], command=lambda: dessert.show())
check_Condements = CheckBox(optional, text="Condements", grid=[1, 8], command=lambda: ketchup.show())
next_btn = PushButton(optional, text="Next", padx=100, pady=10, command=payment_window)

# Payment window
payment = Window(main_app, title="Payment",width=400, height=400,visible=False, layout="grid")
text_tip = Text(payment, text="Tip Amount:", grid=[0, 1])
text_paymethod = Text(payment, text="Payment Method:", grid=[0, 2])
slider = Slider(payment, start=1, end=5, grid=[1, 1])
payment_optns = Combo(payment, options=["None Selected", "Credit", "Debit", "Cash"], selected="None Selected", grid=[1, 2])
next_btn = PushButton(payment, text="Next", padx=100, pady=10, command=summary_window, grid=[1, 3])

#Summary window
summary = Window(main_app, title="Summary", width=800, height=800,visible=False)

#images
loaf = Picture(summary, image="assets\loaf.png", width=100, height=100, visible=False)
piece_toast = Picture(summary, image="assets\piece_toast.png", width=100, height=100, visible=False)
piece_french_toast = Picture(summary, image="assets\piece_french_toast.png", width=100, height=100, visible=False)
dessert = Picture(summary, image="assets\dessert.png", width=100, height=100, visible=False)
drink = Picture(summary, image="assets\drink.png", width=100, height=100, visible=False)
ketchup = Picture(summary, image="assets\ketchup.png", width=100, height=100, visible=False)




main_app.display()