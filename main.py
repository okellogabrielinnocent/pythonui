from tkinter import *

# creats blank window
root = Tk()

# label
# theLabel = Label(root,text="Home of the God's on earth")
# position
# pack puts it to where it finds
# theLabel.pack()
# mainloop keeps the window open till it's closed
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# add widgets

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 1", fg="purple")

# pack widgets to display
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
