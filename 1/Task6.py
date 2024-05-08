# 6. Нахождение максимального элемента в списке:
# Программа находит и выводит самый большой элемент в списке.


number_list = [10, 20, 30, 40]
maximum = 0

for number in number_list:
    if number > maximum:
        maximum = number
print(maximum)


