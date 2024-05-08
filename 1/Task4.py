# 4. Вычисление длины гипотенузы:
# Пользователь вводит длины катетов прямоугольного треугольника, а программа вычисляет и выводит длину гипотенузы по формуле теорема Пифагора.
from math import sqrt


number1 = int(input("Введите длину первого катета:"))
number2 = int(input("Введите длину второго катета:"))

summa = number1*number1+number2*number2

summa2 =summa **0.5

print("Gipotinuza", sqrt(summa))
print("Длина Гипотенузы равна:", summa2)