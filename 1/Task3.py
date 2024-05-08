# 3. Нахождение наименьшего числа:
# Программа принимает три целых числа от пользователя и выводит значение наименьшего из них.

integer1 = int(input("Введите первое число:"))
integer2 = int(input("Введите второе число:"))
integer3 = int(input("Введите третье число:"))


if integer1 < integer2 < integer3:
    print(integer1)
elif integer2 < integer3 < integer1:
    print(integer2)
elif integer3 < integer1 < integer2:
    print(integer3)



