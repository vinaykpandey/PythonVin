from tkinter import *
root = Tk()
root.title("Layout Basic")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

l1 = Label(root, text="First")
l2 = Label(root, text="Second")
l3 = Label(root, text="Third")
l4 = Label(root, text="Fourth")

l1.pack(side=RIGHT)
l2.pack(side=LEFT)
l3.pack(side=BOTTOM)
l4.pack(side=TOP)

root.mainloop()