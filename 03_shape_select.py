# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def input_shape():
    id_shape = input('Введите желаемую фигуру: ')
    while int(id_shape) not in range(0, 4):
        print('Вы ввели некоррректный номер!')
        id_shape = input('Введите желаемую фигуру: ')
    return int(id_shape)

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

shapes = {'треугольник': triangle, 'квадрат': square, 'пятиугольник': pentagon, 'шестиугольник': hexagon}

print('Возможные фигуры:')
for id_shape, shape in enumerate(shapes.keys()):
    print(id_shape, shape)
chosen_shape = input_shape()

for id_shape, shape in enumerate(shapes.keys()):
    if chosen_shape == id_shape:
        shapes[shape](start_point=sd.get_point(100, 100), angle=0, length=100)

sd.pause()
