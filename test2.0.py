from guizero import *

def thing():
    new_window = Window(main, "AHHHH", visible=False)
    new_window.show()
main = App()
text = TextBox(main, "AHHHHH",command="thing")

main.display()
