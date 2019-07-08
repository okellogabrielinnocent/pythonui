from tkinter import *

# creats blank window
root = Tk()

# label
# theLabel = Label(root,text="Home of the God's on earth")
# position
# pack puts it to where it finds
# theLabel.pack()
# mainloop keeps the window open till it's closed


def print_name():
    print("Gabriel Innocent Rockerfeller")


button_1 = Button(root, text="Name", command=print_name)
button_1.pack()

# using bind() to bind and event to a function


def print_user_name(event):
    print("Gabriel Innocent")


button_2 = Button(root, text="Name Binder")
button_2.bind("<Button-1>", print_user_name)
button_2.pack()

root.mainloop()
