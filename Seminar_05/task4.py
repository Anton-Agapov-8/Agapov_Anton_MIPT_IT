from tkinter import *
from tkinter import ttk


def rgb_hex(r, g, b):
    r_hex = str(hex(int(r)))[2:]
    g_hex = str(hex(int(g)))[2:]
    b_hex = str(hex(int(b)))[2:]
    if len(r_hex) == 1:
        r_hex = '0' + r_hex
    if len(g_hex) == 1:
        g_hex = '0' + g_hex
    if len(b_hex) == 1:
        b_hex = '0' + b_hex
    return r_hex, g_hex, b_hex


def calculate():
    try:
        r_in, g_in, b_in = r_entry.get(), g_entry.get(), b_entry.get()
        r_hex, g_hex, b_hex = rgb_hex(r_in, g_in, b_in)
        r_hex2, g_hex2, b_hex2 = rgb_hex(str(255 - int(r_in)), str(255 - int(g_in)), str(255 - int(b_in)))
        print(r_hex, g_hex, b_hex)
        color_in_label.config(text="Заданный Цвет: " + f'#{r_hex + g_hex + b_hex}', bg=f'#{r_hex + g_hex + b_hex}')
        color_res_label.config(text="Комплиментарный цвет: " + f'#{r_hex2 + g_hex2 + b_hex2}',
                               bg=f'#{r_hex2 + g_hex2 + b_hex2}')
    except ValueError:
        pass


root = Tk()
root.title("Комплиментарные цвета")

mainframe = ttk.Frame(root, padding="15 15 15 15")
mainframe.grid(column=0, row=0, sticky='NWES')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

Button(mainframe, text="Calculate", command=calculate).grid(column=100, row=4, sticky=W)

Label(mainframe, text='R').grid(column=1, row=1, sticky='NWES')
Label(mainframe, text='G').grid(column=3, row=1, sticky='NWES')
Label(mainframe, text='B').grid(column=5, row=1, sticky='NWES')
r_entry = Entry(mainframe)
r_entry.grid(column=2, row=1, sticky='NWES')
g_entry = Entry(mainframe)
g_entry.grid(column=4, row=1, sticky='NWES')
b_entry = Entry(mainframe)
b_entry.grid(column=6, row=1, sticky='NWES')

color_in_label = Label(mainframe, text="Заданный Цвет: ")
color_in_label.grid(column=2, row=2, sticky='NWES')

color_res_label = Label(mainframe, text="Комплиментарный цвет: ")
color_res_label.grid(column=2, row=3, sticky='NWES')

result_text = StringVar()
result_color = StringVar()
res_label = Label(mainframe)
res_label.grid(column=1, row=3, sticky='NWES')
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

r_entry.focus()

root.mainloop()
