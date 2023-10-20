from guizero import App, TextBox, PushButton, Text, CheckBox, Window, ButtonGroup, Combo

def calculate_extras():
  total = 0

  if cookies.value == 1:
    total += 15
  if icecream.value == 1:
    total += 10
  if steak.value == 1:
    total += 50
  if wine.value == 1:
    total += 50
  if coffee.value == 1:
    total += 5
  if pop.value == 1:
    total += 15
  if water.value == 1:
    total += 5
  cost.value = total



def second_button():
  window3.show()
def update_text():
  what_is_selected.value = meals.value
def fourth_button():
  window4.show()
def fourth_button():
  button4 = PushButton(window4, command=fourth_button, text="next")
def first_button():  
  window2.show()
def third_button():
  button3 = PushButton(window3, command=third_button, text="next")
def update_text():
  what_is_selected.value = meals.value
def you_chose(selected_value):
  if selected_value == "pay options":
    result.value = "what kind of pay options you chose"
  else:
    result.value = "you chose"


app = App(title="main window")
Text(app, text="whats your name?  ", height=1, width=30)
name = TextBox(app, text="", height=1, width=30)
Text(app, text="what grade are you in? ")
input_box = TextBox(app, text="", height=1, width=30)
window2 = Window(app, title="new window",
                 visible=False)  
what_is_selected = Text(window2, text=50)
button = PushButton(app, command=first_button, text="next")

window3 = Window(app, title="third window", visible=False)

button2 = PushButton(window2, command=second_button, text="next")

meals = ButtonGroup(window2,
                    options=[["steak and patotos", "$50"],
                             ["wings and fies", "$20"],
                             ["sub and cookies", "$10"]],
                    selected="steak and patotos",
                    command=update_text)
window3 = Window(app, title="third window", visible=False)
questions = Text(window3, text="What would you like to eat ?")

cookies = CheckBox(window3, text="cookies ($15)", command=calculate_extras)
icecream = CheckBox(window3, text="icecream ($10)", command=calculate_extras)
steak = CheckBox(window3, text="steak ($50)", command=calculate_extras)
wine = CheckBox(window3, text="wine ($50)", command=calculate_extras)
pop = CheckBox(window3, text="pop ($15)", command=calculate_extras)
water = CheckBox(window3, text="water ($5)", command=calculate_extras)
coffee = CheckBox(window3, text="coffee ($5)", command=calculate_extras)
cost_of_extras = Text(window3, text="Cost of extras:")
cost = TextBox(window3, text=0)

button4 = PushButton(window3, command=fourth_button, text="next")

window4 = Window(app, title="fourth window", visible=False)

instructions = Text(window4, text="Choose a payment method")
combo = Combo(window4,
              options=["", "cash", "debit", "credit"],
              command=you_chose)
result = Text(window4)

total = (int(what_is_selected.value) + int(cost.value))
cost1 = Text(window4, text=f"${total}")
app.display()
