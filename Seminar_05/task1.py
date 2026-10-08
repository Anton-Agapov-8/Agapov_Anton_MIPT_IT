from tkinter import *
from tkinter import ttk

imt_res = -1

s = ''


def calculate():
    try:
        result = '=   ' + str(eval(s.get()))
    except Exception:
        result = 'Error'
    res.set(result)


def add_num(x):
    s.set(s.get() + str(x))


def add_plus():
    s.set(s.get() + '+')


def add_minus():
    s.set(s.get() + '-')


def add_mult():
    s.set(s.get() + '*')


def add_dev1():
    s.set(s.get() + '//')


def add_dev2():
    s.set(s.get() + '%')


def clear():
    s.set('')


def delete_last():
    s.set(s.get()[:-1])


def add_bracket1():
    s.set(s.get() + '(')


def add_bracket2():
    s.set(s.get() + ')')


root = Tk()

root.title("Калькулятор")

mainframe = ttk.Frame(root, padding="10 10 10 10", width=400, height=400)
mainframe.grid(column=0, row=0, sticky='NWES')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=2)
mainframe.columnconfigure(3, weight=1)
number_btns = []
btn_funcs = [lambda: add_num(0),
             lambda: add_num(1),
             lambda: add_num(2),
             lambda: add_num(3),
             lambda: add_num(4),
             lambda: add_num(5),
             lambda: add_num(6),
             lambda: add_num(7),
             lambda: add_num(8),
             lambda: add_num(9)]
for i in [0, *range(1, 10)]:
    if i == 0:
        btn = Button(mainframe, text=str(i), command=btn_funcs[i])
        btn.grid(column=2, row=4)
        number_btns.append(btn)
    else:
        btn = Button(mainframe, text=str(i), command=btn_funcs[i])
        btn.grid(column=(i - 1) % 3 + 1, row=(i - 1) // 3 + 1)
        number_btns.append(btn)

btn_plus = Button(mainframe, text='D', command=delete_last)
btn_plus.grid(column=4, row=1, sticky='NWES')
btn_minus = Button(mainframe, text='C', command=clear)
btn_minus.grid(column=5, row=1, sticky='NWES')
btn_plus = Button(mainframe, text='+', command=add_plus)
btn_plus.grid(column=4, row=2, sticky='NWES')
btn_minus = Button(mainframe, text='-', command=add_minus)
btn_minus.grid(column=5, row=2, sticky='NWES')
btn_multiply = Button(mainframe, text='*', command=add_mult)
btn_multiply.grid(column=4, row=3, sticky='NWES')
btn_devide1 = Button(mainframe, text='//', command=add_dev1)
btn_devide1.grid(column=5, row=3, sticky='NWES')
btn_devide2 = Button(mainframe, text='%', command=add_dev2)
btn_devide2.grid(column=4, row=4, sticky='NWES')
btn_equal = Button(mainframe, text='=', command=calculate)
btn_equal.grid(column=5, row=4, sticky='NWES')

btn_bracket1 = Button(mainframe, text='(', command=add_bracket1)
btn_bracket1.grid(column=1, row=4, sticky='NWES')
btn_bracket2 = Button(mainframe, text=')', command=add_bracket2)
btn_bracket2.grid(column=3, row=4, sticky='NWES')

s = StringVar()
s_label = ttk.Label(mainframe, width=12, textvariable=s)
s_label.grid(column=0, row=0, columnspan=4, sticky='NWES')

res = StringVar()
res.set('=   ')
res_label = Label(mainframe, textvariable=res)
res_label.grid(column=4, row=0, columnspan=2, sticky='NWES')

for child in mainframe.winfo_children():
    child.grid_configure(padx=2, pady=2)

mainframe.pack(fill=X, expand=True)
root.mainloop()
