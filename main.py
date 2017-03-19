from tkinter import *
from PIL import Image, ImageTk
import numpy as np


root = Tk()

# lblName = Label(root, text="Hey there")
# lblName.pack()

cvs = Canvas(root, width=512, height=512)
cvs.pack()

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[256, 256] = [255, 0, 0]
data[256, 128] = [255, 0, 0]
data[128, 256] = [255, 0, 0]
data[128, 128] = [255, 0, 0]

for i in range(1, 8):
    for j in range(1, 8):
        data[i, j] = [255, 0, 0]


img = Image.fromarray(data, 'RGB')
img.save('test.png')

img2 = Image.open("test.png")
tk_img = ImageTk.PhotoImage(img2)

cvs.create_image(250, 250, image=tk_img)
root.mainloop()