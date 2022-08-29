# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle(start_point, angle, length):
    v1 = sd.get_vector(start_point, angle, length)
    v1.draw()

    v2 = sd.get_vector(v1.end_point, angle+120, length)
    v2.draw()

    v3 = sd.get_vector(v2.end_point, angle+240, length)
    v3.draw()


def square(start_point, angle, length):
    v1 = sd.get_vector(start_point, angle, length)
    v1.draw()

    v2 = sd.get_vector(v1.end_point, angle+90, length)
    v2.draw()

    v3 = sd.get_vector(v2.end_point, angle+180, length)
    v3.draw()

    v4 = sd.get_vector(v3.end_point, angle+270, length)
    v4.draw()


def pentagon(start_point, angle, length):
    v1 = sd.get_vector(start_point, angle, length)
    v1.draw()

    v2 = sd.get_vector(v1.end_point, angle+70, length)
    v2.draw()

    v3 = sd.get_vector(v2.end_point, v2.angle+73, length)
    v3.draw()

    v4 = sd.get_vector(v3.end_point, v3.angle+72, length)
    v4.draw()

    v5 = sd.get_vector(v4.end_point, v4.angle+71, length)
    v5.draw()


def hexagon(start_point, angle, length):
    v1 = sd.get_vector(start_point, angle, length)
    v1.draw()

    v2 = sd.get_vector(v1.end_point, angle+60, length)
    v2.draw()

    v3 = sd.get_vector(v2.end_point, v2.angle+60, length)
    v3.draw()

    v4 = sd.get_vector(v3.end_point, v3.angle+60, length)
    v4.draw()

    v5 = sd.get_vector(v4.end_point, v4.angle+60, length)
    v5.draw()

    v6 = sd.get_vector(v5.end_point, v5.angle+60, length)
    v6.draw()


start_point_triangle = sd.get_point(200, 300)
triangle(start_point=start_point_triangle, angle=100, length=200)

start_point_square = sd.get_point(400, 300)
square(start_point=start_point_square, angle=20, length=100)

start_point_pentagon = sd.get_point(100, 100)
pentagon(start_point=start_point_pentagon, angle=0, length=100)

start_point_hexagon = sd.get_point(400, 100)
hexagon(start_point=start_point_hexagon, angle=40, length=50)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

