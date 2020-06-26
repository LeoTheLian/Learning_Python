from tkinter import *


root = Tk()

def display_message():
    message_to_show = Label(root, text = 'Fuck you')
    message_to_show.pack()

# creating a label widget
my_button = Button(root, text = 'Click me', command = display_message)
my_button.pack()

# showing on screen
root.mainloop() 