from tkinter import *


window = Tk()

window.title("Simple Notepad")


def save():
    if t1_value.get() == "":
        t1.insert(END, "Please add text to save it")
    else:
        t1_value.get().save("New-file-1.txt")


t1_value = StringVar()
t1 = Text(window)
t1.grid(row=0, column=0, columnspan=6, padx=7, pady=7)

b1 = Button(window, text="Close", width=15, command=window.destroy)
b1.grid(row=1, column=0, padx=7, pady=7)

b2 = Button(window, text="Copy", width=15)
b2.grid(row=1, column=1, padx=7, pady=7)

b3 = Button(window, text="Paste", width=15)
b3.grid(row=1, column=2, padx=7, pady=7)

b4 = Button(window, text="Save", width=15, command=save)
b4.grid(row=1, column=3, padx=7, pady=7)

window.mainloop()
