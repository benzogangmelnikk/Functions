import simple_draw as sd


# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def vectors(start_point, angle, length, sides=3, angle_variation=0):
    vector = ()
    for side in range(0, sides):
        if side == 0:
            vector = sd.get_vector(start_point, angle, length)
        else:
            vector = sd.get_vector(vector.end_point, vector.angle + angle_variation, length)
        vector.draw()


def triangle(start_point, angle, length):
    vectors(start_point, angle, length, 3, 360 / 3)


def square(start_point, angle, length):
    vectors(start_point, angle, length, 4, 360 / 4)


def pentagon(start_point, angle, length):
    vectors(start_point, angle, length, 5, 360 / 5)


def hexagon(start_point, angle, length):
    vectors(start_point, angle, length, 6, 360 / 6)


start_point_triangle = sd.get_point(200, 300)
triangle(start_point=start_point_triangle, angle=100, length=200)

start_point_square = sd.get_point(400, 300)
square(start_point=start_point_square, angle=20, length=100)

start_point_pentagon = sd.get_point(100, 100)
pentagon(start_point=start_point_pentagon, angle=0, length=100)

start_point_hexagon = sd.get_point(400, 100)
hexagon(start_point=start_point_hexagon, angle=40, length=50)

sd.pause()
