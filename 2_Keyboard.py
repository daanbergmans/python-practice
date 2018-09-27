from keyboard import is_pressed
from time import sleep
from tkinter import *

master = Tk()
label = Label(master, text="Test")
label.pack()

while True:
    key_1 = input("Give key 1: ")
    key_2 = input("Give key 2: ")
    key_3 = input("Give key 3: ")
    key_4 = input("Give key 4: ")
    if len(key_1) == 1 and len(key_2) == 1 and len(key_3) == 1 and len(key_4) == 1:
        print("Keys set!")
        break
    else:
        print("Make sure all your keys are 1 character!")

mainloop()
