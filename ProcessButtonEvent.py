from tkinter import *
def processOK():
    print("OK button is clicked")
def processCancel():
    print("Cancel button is clicked")
window = Tk()
btOK = Button(window, text = "OK", fg = "red", command = processOK )
btCancel = Button(window, text = "Cancel", bg = "yellow", command = processCancel)
btOK.pack()
btCancel.pack()
window.mainloop()