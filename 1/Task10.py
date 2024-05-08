# 10. Угадай рандомное число:
# Программа генерирует случайное число и предлагает пользователю угадать его.
# При каждой попытке программа подсказывает, больше или меньше загаданное число введенного пользователем числа.

import random
random_number = random.randint(1, 101)
while True:
    try:
        number = int(input("Введите число:"))
    except ValueError:
        print("Вы ввели не число")
        break
    if number > random_number:
        print("Загаданное число меньше")
    elif number < random_number:
        print("Загаданное число больше")
    else:
        print("Вы угадали")
        break



