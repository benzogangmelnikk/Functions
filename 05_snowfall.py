# -*- coding: utf-8 -*-

import simple_draw as sd

x_cords = []
y_cords = []
length_list = []
N = 20
random_wind = []

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок


for k in range(0, N):
    x_cords.append(sd.random_number(0, 1100))
    y_cords.append(sd.random_number(200, 1000))
    length_list.append(sd.random_number(10, 100))

start_x_cord = x_cords[:]
start_y_cord = y_cords[:]
start_length = length_list[:]

# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

sd.resolution = (1200, 800)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


while True:
    sd.start_drawing()
    for j in range(0, len(x_cords)):
        if y_cords[j] > 30 and random_wind:
            sd.snowflake(sd.get_point(x_cords[j] - random_wind[j], y_cords[j] + 25), length_list[j], sd.background_color)
    random_wind = []
    for i in range(0, len(x_cords)):
        random_wind.append(sd.random_number(-25, 25))
        sd.snowflake(sd.get_point(x_cords[i], y_cords[i]), length_list[i], sd.COLOR_WHITE)
        if y_cords[i] <= 20:
            y_cords.remove(y_cords[i])
            y_cords.append(start_y_cord[i])

            x_cords.remove(x_cords[i])
            x_cords.append(start_x_cord[i])

            length_list.remove(length_list[i])
            length_list.append(start_length[i])

            continue
        y_cords[i] -= 25
        if x_cords[i] >= 1300:
            continue
        x_cords[i] += random_wind[i]
    sd.finish_drawing()
    sd.sleep(0.6)
    if sd.user_want_exit():
        break
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


