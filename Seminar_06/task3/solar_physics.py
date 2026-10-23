from random import randint

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body != obj:
            dist_square = (body.x - obj.x) ** 2 + (body.y - obj.y) ** 2

            body.Fx -= gravitational_constant * (body.m * obj.m) / dist_square * (body.x - obj.x) / (
                    dist_square ** 0.5)
            body.Fy -= gravitational_constant * (body.m * obj.m) / dist_square * (body.y - obj.y) / (
                    dist_square ** 0.5)
        # r = randint(1, 100) / 100
        # body.Fx += -randint(1, 100) / 100
        # body.Fy += -randint(1, 100) / 100


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    k = 1  # 1000000
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax * dt * k
    body.Vy += ay * dt * k
    body.x += body.Vx * dt * k
    body.y += body.Vy * dt * k
    # print(body.Vx * dt, body.Vy * dt)


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


def calculate_angular_and_area_speed(body, space_objects):
    for obj in space_objects:
        if obj.type == 'star':
            dist = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
            angular_speed = (body.Vx ** 2 + body.Vy ** 2) / dist
            area_speed = 0.5 * dist ** 2 * angular_speed
            return angular_speed, area_speed
    return -1, -1


if __name__ == "__main__":
    print("This module is not for direct call!")
