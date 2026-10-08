from random import choice

import pandas as pd
from tkinter import *
from tkinter import ttk

films = pd.read_csv('imdb_top_250.csv')
genres_list = list(films['Genre'])
film_list = list(films['Title'])
film_genres_dict = {}

for i in range(len(genres_list)):
    genres = list(genres_list[i].split(' | '))
    for genre in genres:
        if genre not in film_genres_dict:
            film_genres_dict[genre] = [film_list[i]]
        else:
            film_genres_dict[genre].append(film_list[i])


def get_genres():
    import pandas as pd

    films = pd.read_csv('imdb_top_250.csv')
    film_genres_list = list(films['Genre'])

    complex_genres = []
    for film_genre in film_genres_list:
        genres = film_genre.split(' | ')
        if len(genres) > 1:
            for genre in genres:
                film_genres_list.append(genre)
            complex_genres.append(film_genre)

    for genre in complex_genres:
        film_genres_list.remove(genre)

    genres_set = set(film_genres_list)
    return sorted(list(genres_set))


def find_random_film():
    try:
        random_film.config(text=f'Случайный фильм: {choice(film_genres_dict[genre_combo.get()])}')
    except ValueError:
        pass


root = Tk()
root.title("Случайный фильм")

mainframe = ttk.Frame(root, padding="15 15 15 15")
mainframe.grid(column=0, row=0, sticky='NWES')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

Button(mainframe, text="Найти фильм", command=find_random_film).grid(column=100, row=4, sticky=W)

genres = get_genres()
# print(genres)

genre_combo = ttk.Combobox(mainframe, values=genres, state="readonly")
genre_combo.grid(column=2, row=1, sticky='NWES')

random_film = Label(mainframe, text="Случайный фильм: ")
random_film.grid(column=2, row=2, sticky='NWES')

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
