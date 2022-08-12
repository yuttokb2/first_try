from tkinter import *

# We create the tk object
root = Tk()
root.title('Scientific Calculator by yuttokb2')
# This allows us to change the background color for any we want to
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

entryfield = Entry(root, font = ('arial',22,'bold'), bg = 'dodgerblue3', fg = 'white',bd = 10,relief=SUNKEN, width=30)
entryfield.grid(row=0,column=0)


button = Button(root, width = 5, height = 2, bd = 2, relief = SUNKEN, text = 'C')
button.grid(row = 1, column = 0)
# This instance let us keep the window in a continue loop, which means that it will not close
# unless we close it.

root.mainloop()
