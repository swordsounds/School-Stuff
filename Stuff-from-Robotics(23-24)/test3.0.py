from guizero import *
primary = 0
def open_window():
  First_name.value = input_box.value
  Last_name.value = input_box2.value
  Grade_level.value = input_box3.value
  app.hide()
  window2.show()

def open_window2():
  window2.hide()
  window3.show()
def open_window3():
  window3.hide()
  window4.show()
def open_window4():
  window4.hide()
  window5.show()
def open_window5():
  window5.hide()
  window6.show()
def open_window6():
  window6.hide()
  window7.show()
def open_window7():
  window7.hide()
  window8.show()
def open_window8():
  window8.hide()
  if option.value=="5":
    picture=Picture(window9, image="hamcheese2.png")
  window9.show()



def update_calculation():
  what_is_selected.value = option.value

def calculate_extras():
  total = 0
  if chocolate_pudding.value == 1:
    total += 2
  elif coca_cola.value == 1:
    total += 1
  elif fruit_salad.value == 1:
    total += 3
  cost.value = total
def primary_cost():

    if option.value == "Ham & cheese sandwhich":
        primary = 5
    elif option.value == "Chicken nuggets":
        primary = 3
    elif option.value == "Slice of pizza":
        primary = 4
    
    if chocolate_pudding.value == 1:
        secondary = 2
    elif coca_cola == 1:
        secondary = 1
    elif fruit_salad.value == 1:
        secondary = 3
    payp = text(summarize, text=f"1st {primary}")
    pays = text(summarize, text=f"1st {secondary}")


def slider_changed(slider_value):
  textbox.value = slider_value + "%"
app = App(title="Window 1")
text = Text(app, text="Please type your first name below:")
input_box = TextBox(app, text="")

text = Text(app, text="Please type your last name below:")
input_box2 = TextBox(app, text="")

text = Text(app, text="Please type your grade level below:")
input_box3 = TextBox(app, text="")
open_button = PushButton(app, text="Next", command=open_window)


window2 = Window(app, title="Window 2", visible=False)
First_name = Text(window2, text="Your first name is:")
Last_name = Text(window2, text="Your last name is:")
Grade_level = Text(window2, text="Your grade level is:")
open_button2 = PushButton(window2, text="Next", command=open_window2)

window3 = Window(app, title="Window 3", visible=False)
text = Text(window3, text="Please pick a lunch option:")
option = ButtonGroup(window3, options=["Ham & cheese sandwich","Slice of pizza","Chicken nuggets"], selected="Ham & cheese sandwich")
text = Text(window3, text="Total cost of meal:")
what_is_selected = TextBox(window3, text="5")
open_button3 = PushButton(window3, text="Next", command=open_window3)

window4 = Window(app, title="Window 4", visible=False)
text = Text(window4, text="Pick what you want with your lunch:")
chocolate_pudding = CheckBox(window4,text="Chocolate pudding ($2)")
coca_cola = CheckBox(window4, text="Coca-cola ($1)")
fruit_salad = CheckBox(window4,text="Fruit salad ($3)")
text = Text(window4, text="Total cost of extras:")
cost = TextBox(window4, text="0")
open_button4 = PushButton(window4, text="Next", command=open_window4)

window5 = Window(app, title="Window 5", visible=False)
text = Text(window5,text="The total cost of all of your selected items without tip is:")
without_addon = TextBox(window5, text=primary)
open_button5 = PushButton(window5, text="Next", command=open_window5)

window6 = Window(app, title="Window 6", visible=False)
instrucions = Text(window6, text="Please choose a payment option:")
combo = Combo(window6, options=["", "Cash", "Credit Card", "Debit Card"])
open_button6 = PushButton(window6, text="Next", command=open_window6)

window7 = Window(app, title="Window 7", visible=False)
text = Text(window7, text="Your chosen payment option is:")
text = Text(window7,text="This is the percentage of the tip that you want to give:")
slider = Slider(window7, start=15, end=100, command=slider_changed)
textbox = TextBox(window7, text="0")
open_button7 = PushButton(window7, text="Next", command=open_window7)

window8 = Window(app, "window8")
text = Text(window8, text="The tip that you have chosen to give is:")
text = Text(window8, text="This is the total cost of your meal with tip:")
primary_text = Text(window8, text="")
secondary_text = Text(window8, text="")
open_button8 = PushButton(window8, text="Pay", command=open_window8)


window9 = Window(app, title="Window 9", visible=False)

summarize = Window(app, title="Summarize", visible=False)

app.display()











