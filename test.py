from guizero import App, Text

# Action you would like to perform
def counter():
    text.value = int(text.value) + 1

app = App("Hello world")
text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms
app.display()


# from guizero import *
# import random


# def read_sensor():
#     return random.randrange(3200, 5310, 10) / 100


# def update_label():
#     text.set(read_sensor())
#     # recursive call
#     text.after(1000, update_label)


# if __name__ == '__main__':
#     app = App(title='Sensor Display!',
#               height=100,
#               width=200,
#               layout='grid')

#     title = Text(app, 'Sensor value:', grid=[0, 0])
#     text = Text(app, "xx", grid=[1, 0])

#     text.after(1000, update_label)
#     app.display()