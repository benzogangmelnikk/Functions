# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_branches(start_point, angle, length):
	if length < 3:
		return
	min_angle_delta = 30 - 30 * 0.4
	max_angle_delta = 30 + 30 * 0.4
	new_angle_1 = angle - sd.random_number(min_angle_delta, max_angle_delta)
	new_angle_2 = angle + sd.random_number(min_angle_delta, max_angle_delta)
	b1 = sd.get_vector(start_point, new_angle_1, length)
	b1.draw()
	b2 = sd.get_vector(start_point, new_angle_2, length)
	b2.draw()
	length_delta = sd.random_number(-15, 15) / 100
	new_b1_point = b1.end_point
	draw_branches(new_b1_point, new_angle_1, length * (0.75 + length_delta))
	new_b2_point = b2.end_point
	draw_branches(new_b2_point, new_angle_2, length * (0.75 + length_delta))
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


root_point = sd.get_point(300, 30)
draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


