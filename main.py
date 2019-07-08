from tkinter import *

#creats blank window
root = Tk()

#label
# theLabel = Label(root,text="Home of the God's on earth")
#position
#pack puts it to where it finds
# theLabel.pack()
#mainloop keeps the window open till it's closed

# left click and right click
def left_click(event):
	print("Left click")
def right_click(event):
	print("Right click")
def middle_click(event):
	print("Middle Click")

#invisible frame
frame = Frame(root,width =300, height=250)
frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)
frame.pack()

root.mainloop()

