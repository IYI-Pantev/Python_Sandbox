from tkinter import *


window = Tk()

window.title("CA$ to BGN")
window.minsize(width=320, height=220)
window.config(padx=25, pady=25)

#Canvas
canvas = Canvas(width=512, height=358)

flag = PhotoImage(file="canada-flag-icon.png")
canvas.create_image(512, 358, image=flag)
canvas.place(anchor=CENTER)
# Label equals to...

expl_label = Label(text="is equal to")
expl_label.config(padx=15, pady=15)
expl_label.grid(column=0, row=1)

# Entry

entry = Entry()
entry.config(width=10)

entry.grid(column=1, row=0)

# Label bgn equals
bgn_label = Label(text="0")
bgn_label.config(padx=15, pady=15)
bgn_label.grid(column=1, row=1)


# Button calculate
def calculate():
    cad = float(entry.get())
    lev = round(cad * 1.35, 2)
    bgn_label.config(text=f"{lev}")


button = Button(text="Calculate", command=calculate)
button.config(padx=10, pady=10)

button.grid(column=1, row=2)

# Label CAD

cad_label = Label(text="Canadian Dollar")
cad_label.config(padx=10, pady=10)
cad_label.grid(column=2, row=0)

# Label BGN
lev_label = Label(text="Bulgarian Lev")
lev_label.config(padx=10, pady=10)
lev_label.grid(column=2, row=1)

window.mainloop()
