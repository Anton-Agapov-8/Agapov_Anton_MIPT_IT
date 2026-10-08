from tkinter import *
from tkinter import ttk

imt_res = -1


def calculate(*args):
    try:
        global imt_res
        mass = float(mass_entry.get())
        height = float(height_entry.get())
        # print(height, mass)
        imt_res = round(mass / (height / 100) ** 2, 1)
        imt.set(imt_res)
        if imt_res < 16:
            # result_text.set(results[0])
            res_label.config(text=results[0], bg='#0000FF')
        elif 16 <= imt_res < 18.5:
            result_text.set(results[1])
            res_label.config(text=results[1], bg='#00FFFF')
        elif 18.5 <= imt_res < 25:
            result_text.set(results[2])
            res_label.config(text=results[2], bg='#00FF00')
        elif 25 <= imt_res < 30:
            result_text.set(results[3])
            res_label.config(text=results[3], bg='#CCFF00')
        elif 30 <= imt_res < 35:
            result_text.set(results[4])
            res_label.config(text=results[4], bg='#FFFF00')
        elif 35 <= imt_res < 40:
            result_text.set(results[5])
            res_label.config(text=results[5], bg='#FFCC00')
        elif 40 <= imt_res:
            result_text.set(results[6])
            res_label.config(text=results[6], bg='#FF0000')

    except ValueError:
        pass


results = ['Выраженный дефицит массы тела',
           'Недостаточная (дефицит) масса тела',
           'Норма',
           'Избыточная масса тела (предожирение)',
           'Ожирение 1 степени',
           'Ожирение 2 степени',
           'Ожирение 3 степени']

root = Tk()
root.title("IMT")

mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=2)
mainframe.columnconfigure(3, weight=1)

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=1, row=1, sticky=(W, E))

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=3, row=1, sticky=(W, E))

imt = StringVar()
Label(mainframe, textvariable=imt).grid(column=2, row=2, sticky=(W, E))

Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

Label(mainframe, text="Рост").grid(column=2, row=1, sticky=W)
Label(mainframe, text="Масса").grid(column=4, row=1, sticky=W)
Label(mainframe, text="ИМТ: ").grid(column=1, row=2, sticky=E)
Label(mainframe, text="кг/м^2").grid(column=3, row=2, sticky=W)

result_text = StringVar()
result_color = StringVar()
res_label = Label(mainframe)
res_label.grid(column=1, row=3, sticky=W)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

mass_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
