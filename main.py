from tkinter import *

# creats blank window
root = Tk()

# label
# theLabel = Label(root,text="Home of the God's on earth")
# position
# pack puts it to where it finds
# theLabel.pack()
# mainloop keeps the window open till it's closed

# bg is background color while fg is front color
one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
# grows the two widget to parent size on x direction
two.pack(fill=X)

three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)
root.mainloop()
