import tkinter as tk
from tkinter import filedialog
from glob import glob

root = tk.Tk()
root.title('Image Sorter')

global test

def test():
    print(test)

def openFileDialog():
    file_path = filedialog.askdirectory()
    test = "test"
    test()

label = tk.Label(root, text='Select folder: ').pack(side=tk.LEFT)
button = tk.Button(root, text='Select', command=openFileDialog).pack(side=tk.LEFT)

root.mainloop()
