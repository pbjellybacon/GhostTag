from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import pyqrcode


# Create a Tkinter GUI container
root = Tk()
root.wm_title("GhostTag")

# lblName = Label(root, text="Fuck shit up")
# lblName.pack()

cvs = Canvas(root, width=512, height=512)
cvs.pack()

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[256, 256] = [255, 0, 0]
data[256, 128] = [255, 0, 0]
data[128, 256] = [255, 0, 0]
data[128, 128] = [255, 0, 0]

img = Image.fromarray(data, 'RGB')
img.save('test.png')

qr = pyqrcode.create("FUCK BITCHES!")
qr.png("qr1.png", scale=8)

img2 = Image.open("test.png")
tk_img = ImageTk.PhotoImage(img2)

cvs.create_image(250, 250, image=tk_img)
root.mainloop()