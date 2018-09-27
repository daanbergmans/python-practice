import tkinter as tk
import PIL.ImageTk as ImageTk
import PIL.Image as Image

root = tk.Tk()
root.title('Osu! Bongo Cat')

test_images = {
    1: Image.open("img_onKeyDown.gif"),
    2: Image.open("img_onKeyUp.gif")
}

def on_down(e):
    if e.char == 'a':
        base_image = ImageTk.PhotoImage(test_images[2])
        imageLabel.configure(image=base_image)
        imageLabel.image = base_image
        root.update()

def on_up(e):
    if e.char == 'a':
        base_image = ImageTk.PhotoImage(test_images[1])
        imageLabel.configure(image=base_image)
        imageLabel.image = base_image
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

base_image = ImageTk.PhotoImage(test_images[1])

imageLabel = tk.Label(root, image=base_image)
imageLabel.image = base_image

imageLabel.pack(side=tk.LEFT)

root.mainloop()
