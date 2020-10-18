from tkinter import *
root = Tk()
root.title("Set Size")
root.geometry("300x300")
root.wm_minsize(width=200, height=200)
root.wm_maxsize(width=400, height=400)


root.mainloop()