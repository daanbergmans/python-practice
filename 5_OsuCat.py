import tkinter as tk
import PIL.ImageTk as ImageTk
import PIL.Image as Image

root = tk.Tk()
root.title('Osu! Bongo Cat')
root.minsize(825, 200)

key_images = {
    1: Image.open("Images/1000.png"),
    2: Image.open("Images/0100.png"),
    3: Image.open("Images/0010.png"),
    4: Image.open("Images/0001.png"),
}

def on_down(e):
    e.char == k1 and update("show", imageLabel_1000)
    e.char == k2 and update("show", imageLabel_0100)
    e.char == k3 and update("show", imageLabel_0010)
    e.char == k4 and update("show", imageLabel_0001)

def on_up(e):
    e.char == k1 and update("hide", imageLabel_1000)
    e.char == k2 and update("hide", imageLabel_0100)
    e.char == k3 and update("hide", imageLabel_0010)
    e.char == k4 and update("hide", imageLabel_0001)

def update(task, imageLabel):
    if task == "show":
        imageToShow = ImageTk.PhotoImage(key_images[1])
        imageLabel.configure(image=imageToShow)
        imageLabel.image = imageToShow
    elif task == "hide":
        imageLabel.configure(image="")
    root.update()

while True:
    k1 = input("Key 1 is: ")
    k2 = input("Key 2 is: ")
    k3 = input("Key 3 is: ")
    k4 = input("Key 4 is: ")
    if len(k1) == 1 and len(k2) == 1 and len(k3) == 1 and len(k4) == 1:
        print("Key configuration done!")
        break
    else:
        print("Make sure all keys are only 1 character long!")

root.bind('<KeyPress>', on_down)
root.bind('<KeyRelease>', on_up)

imageLabel_1000 = tk.Label(root, image="")
imageLabel_1000.pack(side=tk.LEFT, fill=None, expand=False)
imageLabel_0100 = tk.Label(root, image="")
imageLabel_0100.pack(side=tk.LEFT, fill=None, expand=False)
imageLabel_0010 = tk.Label(root, image="")
imageLabel_0010.pack(side=tk.LEFT, fill=None, expand=False)
imageLabel_0001 = tk.Label(root, image="")
imageLabel_0001.pack(side=tk.LEFT, fill=None, expand=False)

root.mainloop()
