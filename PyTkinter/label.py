from tkinter import *
root = Tk()
root.title("Label Example")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

#creating and placing a label
l1 = Label(root, text="First")
l1.place(x=10, y=10)

# set size, fg, bg, font, text, size, bold
l2 = Label(root, text="Second", fg="lightblue", bg="navy")
l2.config(width=10, height=3, font=("calibri", 16, "bold"))
l2.place(x=100, y=10)

# pic = PhotoImage("path")
# l3 = Label(root, text="Third", image=pic)


root.mainloop()