import tkinter as tk
import PIL.ImageTk as ImageTk
import PIL.Image as Image
import winsound
from time import sleep

root = tk.Tk()
root.title('Bongo James')

playSound = True

key_images = {
    1: Image.open("assets/Bongo_James_1.png"),
    2: Image.open("assets/Bongo_James_2.png")
}

def on_down(e):
    e.char == k1 and update("show") and playSound()
    e.char == k2 and update("show") and playSound()
    playSound = False

def on_up(e):
    e.char == k1 and update("hide")
    e.char == k2 and update("hide")
    playSound = True

def update(task):
    global playSound
    if task == "show":
        setImage(2)
        playSound == True and winsound.PlaySound("assets/Desk_Slam_Cut.wav", winsound.SND_ASYNC)
    elif task == "hide":
        setImage(1)
    root.update()

def setImage(imageIndex):
    imageToShow = ImageTk.PhotoImage(key_images[imageIndex])
    imageLabel.configure(image=imageToShow)
    imageLabel.image = imageToShow

while True:
    k1 = input("Key 1 is: ")
    k2 = input("Key 2 is: ")
    if len(k1) == 1 and len(k2) == 1:
        print("Key configuration done!")
        break
    else:
        print("Make sure all keys are only 1 character long!")

sleep(2)
print("We have all heard of Bongo cat...")
sleep(2)
print("But have you heard...")
sleep(2)
print("Of Bongo James?")
sleep(2)

root.bind('<KeyPress>', on_down)
root.bind('<KeyRelease>', on_up)

imageToShow = ImageTk.PhotoImage(key_images[1])

imageLabel = tk.Label(root, image=imageToShow)
imageLabel.image = imageToShow
imageLabel.pack(side=tk.LEFT)

root.focus_force()

root.mainloop()
