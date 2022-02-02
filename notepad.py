import tkinter as tk
from tkinter import END
from tkinter.filedialog import askopenfilename, asksaveasfilename


# saving the file
def saving_file():
    file_location = asksaveasfilename(defaultextension="txt",
                                      filetypes=[("Text files", "*.txt"), ["All files", "*.*"]])

    if not file_location:
        return
    with open(file_location, "w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    para.title(f"Notepad - {file_location}")


def opening_file():
    file_location = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    para.title(f"Notepad - {file_location}")


para = tk.Tk()
para.title("Notepad")
para.rowconfigure(0, minsize=1000)
para.columnconfigure(1, minsize=1000)

b1 = tk.Button(para, text="Close", width=15, command=para.destroy)
b1.grid(row=1, column=0, padx=7, pady=7)

b2 = tk.Button(para, text="Copy", width=15)
b2.grid(row=1, column=1, padx=7, pady=7)

b3 = tk.Button(para, text="Paste", width=15)
b3.grid(row=1, column=2, padx=7, pady=7)

b4 = tk.Button(para, text="Save", width=15)
b4.grid(row=1, column=3, padx=7, pady=7)

text_edit = tk.Text(para)
text_edit.grid(row=0, column=1, sticky="nsew")

frame_button = tk.Frame(para, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

button_open = tk.Button(frame_button, text="OPEN FILE", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = tk.Button(frame_button, text="SAVE AS", command=saving_file)
button_save.grid(row=1, column=0, padx=5)

para.mainloop()
