from tkinter import *
root = Tk()
root.title("Radiobutton Clicked Example")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

def setColor():
    c = ["red", "blue", "green"]
    color_index = v.get()-1 # color number 1/2/3
    e1.config(fg=c[color_index])

l1 = Label(root, text="Select your color")
l1.place(x=50, y=40)

v = IntVar()
v.set(1)
rb1 = Radiobutton(root, text="RED", fg="red", variable=v, value=1, command=setColor)
rb2 = Radiobutton(root, text="BLUE", fg="blue",variable=v, value=2, command=setColor)
rb3 = Radiobutton(root, text="GREEN", fg="green",variable=v, value=3,command=setColor)

rb1.place(x=50,y=80,width=80)
rb2.place(x=150,y=80,width=80)
rb3.place(x=250,y=80,width=80)

l2 = Label(root, text="Enter your name")
l2.place(x=50, y=150)

e1 = Entry(root, font=("calibri", 14), fg="maroon", bg="white")
e1.config(borderwidth=2, relief="solid")
e1.place(x=50, y=150)


root.mainloop()