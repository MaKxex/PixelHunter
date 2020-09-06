from tkinter import *
from PIL import ImageTk, Image
root = Tk()

start_pos = None
img = ImageTk.PhotoImage(Image.open("asd.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
def start_mouse_press(event):
    global start_pos
    start_pos = (event.x, event.y)

def stop_mouse_press(event):
    print(f"Start Pos {start_pos}\nEnd Pos {event.x, event.y}")


root.bind("<ButtonPress-1>", start_mouse_press)
root.bind("<ButtonRelease-1>", stop_mouse_press)
mainloop()
