from tkinter import *
root = Tk()
root.title("Set Compnents")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

b1 = Button(root, text="One")
b2 = Button(root, text="Two")

e1 = Entry(root)
cb1 = Checkbutton(root, text="Four")
rb1 = Radiobutton(root, text="Five")


b1.pack()
b2.pack()
e1.pack()
cb1.pack()
rb1.pack()

root.mainloop()