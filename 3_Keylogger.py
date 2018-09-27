import tkinter as tk

root = tk.Tk()
root.title('Keylogger')

def on_down(e):
    file = open("keylogger.txt", "a")
    file.write(e.char)

root.bind('<KeyPress>', on_down)

root.mainloop()
