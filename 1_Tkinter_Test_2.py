import tkinter as tk

root = tk.Tk()

class App:

    def __init__(self, master):

        frame = tk.Frame(master)
        frame.pack()

        self.button = tk.Button(frame, text="QUIT", fg="red", command=frame.quit).pack( side = tk.LEFT )

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi).pack( side = tk.LEFT )

    def say_hi(self):
        print("hi there, everyone!")

app = App(root)

root.mainloop()
