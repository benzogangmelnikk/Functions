# -*- coding: utf-8 -*-
import pygame
import simple_draw
import simple_draw as sd

colors = {'red': sd.COLOR_RED, 'orange': sd.COLOR_ORANGE, 'yellow': sd.COLOR_YELLOW, 'green': sd.COLOR_GREEN,
          'cyan': sd.COLOR_CYAN, 'blue': sd.COLOR_BLUE, 'purple': sd.COLOR_PURPLE}


def input_color():
    id_color = input('Введите желаемый цвет: ')
    while int(id_color) not in range(0, 7):
        print('Вы ввели некоррректный номер!')
        id_color = input('Введите желаемый цвет: ')
    return int(id_color)

def vectors(start_point, angle, length, sides=3, angle_variation=0):
    vector = ()
    for side in range(0, sides):
        if side == 0:
            vector = sd.get_vector(start_point, angle, length)
        else:
            vector = sd.get_vector(vector.end_point, vector.angle + angle_variation, length)
        vector.draw(color=draw_color)


def triangle(start_point, angle, length):
    vectors(start_point, angle, length, 3, 360 / 3)


def square(start_point, angle, length):
    vectors(start_point, angle, length, 4, 360 / 4)


def pentagon(start_point, angle, length):
    vectors(start_point, angle, length, 5, 360 / 5)


def hexagon(start_point, angle, length):
    vectors(start_point, angle, length, 6, 360 / 6)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

print('Возможные цвета:')
for id_color, color in enumerate(colors.keys()):
    print(id_color, color)
chosen_color = input_color()

for id_color, color in enumerate(colors.keys()):
    if id_color == chosen_color:
        draw_color = colors[color]

start_point_triangle = sd.get_point(200, 300)
triangle(start_point=start_point_triangle, angle=100, length=200)

start_point_square = sd.get_point(400, 300)
square(start_point=start_point_square, angle=20, length=100)

start_point_pentagon = sd.get_point(100, 100)
pentagon(start_point=start_point_pentagon, angle=0, length=100)

start_point_hexagon = sd.get_point(400, 100)
hexagon(start_point=start_point_hexagon, angle=40, length=50)

sd.pause()
