import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

datafile_path = ''


def mnk(x, y):
    n = len(x)
    x = np.array(x)
    y = np.array(y)
    x_av = np.sum(x) / n
    y_av = np.sum(y) / n
    xy_av = np.sum(x * y) / n
    xsquare_av = np.sum(x ** 2) / n
    a = (xy_av - x_av * y_av) / (xsquare_av - x_av ** 2)
    b = y_av - a * x_av
    return a, b


def open_datafile():
    global datafile_path
    datafile_path = filedialog.askopenfilename()
    filelabel.config(text=f'Открыты данные из файла: {datafile_path}')


def count():
    if datafile_path:
        graphfile_path = filedialog.asksaveasfilename(
            filetypes=(('PNG Изображение', '*.png'), ('SVG Изображение', '*.svg'), ('EPS Изображение', '*.eps')), defaultextension=".png")
        print(graphfile_path)
        if graphfile_path is not None:

            data = pd.read_csv(datafile_path)
            x = data[data.keys()[0]]
            y = data[data.keys()[1]]

            plt.plot(x, y, 'rD-', linewidth=0, label='Измеренные данные')

            a, b = mnk(x, y)
            bsign = '+'
            if b < 0:
                bsign = '-'
            x2 = np.linspace(min(x), max(x), 100)
            plt.plot(x2, a * x2 + b, ':', linewidth=2, color='#000000',
                     label=f'Аппроксимация МНК: $Y \\approx {a:.3f}X{bsign}{abs(b):.3f}$')
            plt.legend()
            plt.xlabel(data.keys()[0])
            plt.ylabel(data.keys()[1])
            plt.savefig(graphfile_path)
            plt.show()


root = Tk()
root.title("АвтоЛаба")
mainframe = ttk.Frame(root, padding="15 15 15 15")
mainframe.grid(column=0, row=0, sticky='NWES')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)

Button(mainframe, text="Открыть файл с данными", command=open_datafile).grid(column=1, row=2, sticky=W)
Button(mainframe, text="Рассчитать МНК и сохранить график", command=count).grid(column=2, row=2, sticky=E)

filelabel = Label(mainframe, text='Файл с данными не открыт.')
filelabel.grid(column=1, row=1, columnspan=10, sticky='NWES')

root.mainloop()
