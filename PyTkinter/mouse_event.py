from tkinter import *
root = Tk()
root.title("Addition of two number")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

def fun(event):
    l1.config(text=("x=" + str(event.x) + "y=" + str(event.y)))


l1 = Label(root, fg="blue")
l1.place(x=10, y=10)

root.bind('<Motion>', fun)

root.mainloop()