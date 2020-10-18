from tkinter import *
root = Tk()
root.title("Button Example")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

#creating and placing a simple button
b1 = Button(root, text="first")
b1.place(x=10, y=10)

# creating and set size of button
b2 = Button(root, text="Second", width=15, height=5)
b2.place(x=100, y=10)

# creating, setting position and size of button
b3 = Button(root, text="Third")
b3.place(x=10, y=100, width=90, height=30)

# creating and setting background and foreground color of button
b4 = Button(root, text="Fourth", bg="green", fg="white")
b4.place(x=100, y=100, width=100, height=30)

root.mainloop()