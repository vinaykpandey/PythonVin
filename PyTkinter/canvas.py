from tkinter import *
root = Tk()
root.title("Canvas Example")
root.geometry("500x500")
root.wm_minsize(width=300, height=300)

"""
The canvas widget supplies graphics facilities for Tkinter. Among these graphical objects are lines, circles, images,
and even other widgets. With this widget it's possible to draw graphs and plots, create graphics and implement
various kinds of custom widgets
"""
#creating canvas with background color
c = Canvas(root, bg="gray")
c.place(x=10, y=10, width=400, height=400)

#creating grphical objects
c.create_line(20,20,200,20, fill="yellow")
c.create_rectangle(30,30,200,200, fill="lightgreen", outline="red")
c.create_oval(30, 220, 90, 280, fill="red", outline="green")
c.create_polygon(200,220,180,250,220,250, fill="#112233", outline="navy", width=5)

#creating star
pts=[100,140,110,110,140,100,110,90,100,60,90,90,60,100,90,110]
c.create_polygon(pts, fill="yellow")

root.mainloop()