from tkinter import *
root = Tk()
root.title("Entry Example")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

#creating and placing a TextBox
e1 = Entry(root)
e1.place(x=10, y=10)

# creating, placing, sizing, font, color, border
e2 = Entry(root, font=("calibri", 14), fg="maroon", bg="orange")
e2.config(borderwidth=2, relief="solid")
e2.place(x=10, y=40)

#creating Entry with default text and non editable
e3 = Entry(root)
e3.insert(0, "Vinay")
e3.insert(6, " ")
e3.insert(7, "Pandey")
e3.config(state=DISABLED)
e3.place(x=100, y=20)


root.mainloop()