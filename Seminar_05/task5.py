from tkinter import *
from random import randint, randrange


class Ball:
    def __init__(self, x=None, y=None, dx=None, dy=None, R=None, color=None):
        if R is None:
            self.R = randint(10, 50)
        else:
            self.R = R
        if x is None:
            self.x = randint(self.R, root.winfo_width() - self.R)
        else:
            self.x = x
        if y is None:
            self.y = randint(self.R, root.winfo_height() - self.R)
        else:
            self.y = y
        if color is None:
            self.color = 'green'
        else:
            self.color = color
        if dx is None:
            self.dx = 10
        else:
            self.dx = dx
        if dy is None:
            self.dy = 10
        else:
            self.dy = dy

        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill=self.color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > root.winfo_width() or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > root.winfo_height() or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    global balls
    balls.append(Ball(event.x, event.y, randrange(-20, 20), randrange(-20, 20), randint(10, 50), rgb_to_hex((randint(0, 255), randint(0, 255), randint(0, 255)))))


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'300x300')
root.update()

WIDTH = root.winfo_width()
HEIGHT = root.winfo_height()

canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=True)
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for i in range(5)]
tick()
root.mainloop()
