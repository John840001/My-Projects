from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Pixels")
root.configure(bd=10)

lona = Canvas(root, width=650, height=550, bg="Gainsboro")
lona.grid(column=0,row=0,columnspan=3)

def color1(event):
    current = event.widget.find_withtag('current')
    item = current[0]
    lona.itemconfigure(item, fill=color, outline=color)

def color2(event):
    current = event.widget.find_withtag('current')
    item = current[0]
    lona.itemconfigure(item, fill="Ghost White", outline="Giansboro")

def nuevo():
    cuadricula()

color = "Blue Violet"
def paleta():
    global color
    c = colorchooser.askcolor()
    color = c[1]
    button1.configure(bg = color)

def guardar():
    lona.postscript(file = "Pixel_art.eps")

button1 = Button(root,height = 2, bg=color, bd=0, cursor="hand1",command=paleta)
button1.grid(column=0,row=1,columnspan=3,pady=2,sticky=E+W)
button2 = Button(root,height = 2, text="Save", cursor="hand1",command=guardar)
button2.grid(column=0,row=2,sticky=E+W)
button3 = Button(root,height = 2, text="New", cursor="hand1",command=nuevo)
button3.grid(column=1,row=2,sticky=E+W)

def cuadricula():
    for y in range(2,500,15):
        for x in range(2,600,15):
            cua = lona.create_rectangle(x,y,x+15,y+15,fill="Ghost White",width=1,outline="Blue")
            lona.tag_bind(cua,'<Button-1>',color1)
            lona.tag_bind(cua,'<Button-2>',color2)

cuadricula()

root.mainloop()