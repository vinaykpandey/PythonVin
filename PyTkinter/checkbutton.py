from tkinter import *
root = Tk()
root.title("CheckButton Example")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

#creating and placing a CheckBox
cb1 = Checkbutton(root)
cb1.place(x=10, y=10)

# creating, placing, sizing, font, color, border
cb2 = Checkbutton(root, text="Agree")
cb2.config(borderwidth=2, relief="solid")
cb2.place(x=10, y=40)

cb3 = Checkbutton(root, text="Already Selected")
cb3.select()
cb3.config(bg="gray")
cb3.place(x=10, y =80, width=150, height=30)


root.mainloop()