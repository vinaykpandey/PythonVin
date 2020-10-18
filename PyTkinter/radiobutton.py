from tkinter import *
root = Tk()
root.title("Radiobutton Example")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

#creating and placing a Radiobutton
v = IntVar()
v.set(1)
rb1 = Radiobutton(root, text="Tea", variable=v, value=1)
rb2 = Radiobutton(root, text="Coffee", variable=v, value=2)

rb1.place(x=100, y=10)
rb2.place(x=100, y=30)


root.mainloop()