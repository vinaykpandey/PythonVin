from tkinter import *
root = Tk()
root.title("Layout Management")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

l1 = Label(root, text="First", bg="yellow")
l2 = Label(root, text="Second", bg="lightgreen")
l3 = Label(root, text="Third", bg="lightblue")
l4 = Label(root, text="Fourth", bg="pink")


# pack example
# l1.pack(fill=X)
# l1.pack(padx=10, pady=20)
# # l2.pack(fill=X)
# l2.pack(ipadx=10, ipady=20)
# l3.pack(fill=X)
# l4.pack(fill=X)

# grid example
# widh in config function is each character size
l1.config(width=20, height=5)
l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
l3.grid(row=1, column=0)
l4.grid(row=1, column=1)


root.mainloop()