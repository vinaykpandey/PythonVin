from tkinter import *
root = Tk()
root.title("Addition of two number")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

def  sum():
    a = e1.get()
    b  = e2.get()
    s = int(a) + int(b)
    l4.config(text="Sum is %d" %(s))


l1 = Label(root, text="Addition of two number")
l1.place(x=30, y=50)

l2 = Label(root, text="First Number")
l2.place(x=30, y=100)

l3 = Label(root, text="Second Number")
l3.place(x=30, y=150)


e1 = Entry(root, borderwidth=2, relief="solid")
e2 = Entry(root, borderwidth=2, relief="solid")
e1.place(x=150, y=100)
e2.place(x=150, y=150)


b1 = Button(root, text="Add", command=sum)
b1.place(x=50, y=180)

l4 = Label(root, text="Result")
l4.place(x=30, y=240)

root.mainloop()