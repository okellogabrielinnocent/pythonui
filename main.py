from tkinter import *

#creats blank window
root = Tk()

#label
# theLabel = Label(root,text="Home of the God's on earth")
#position
#pack puts it to where it finds
# theLabel.pack()
#mainloop keeps the window open till it's closed

#grid allows putting layout in rows and coluns

label_1 = Label(root,text="Name")
label_2 = Label(root,text="Password")
#entry is used for inputting
entry_1= Entry(root)
entry_2= Entry(root)

#by defualt column is always 0
#stick does alignment using direction N,S,E,W directions
label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

check =Checkbutton(root,text="Keep me signed in")
check.grid(columnspan=2)

root.mainloop()

