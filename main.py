from tkinter import *

# creats blank window
# root = Tk()

# label
# theLabel = Label(root,text="Home of the God's on earth")
# position
# pack puts it to where it finds
# theLabel.pack()
# mainloop keeps the window open till it's closed


class GabsButton:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(
            frame, text="Message", command=self.print_message)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side=LEFT)

    def print_message(self):
        print("We rock. Yeah!!!")


root = Tk()
g = GabsButton(root)

root.mainloop()
