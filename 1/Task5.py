# 5. Вычисление суммы элементов списка:
# Программа вычисляет и выводит сумму всех элементов списка, который вводит пользователь.


number_list = [10, 20, 30, 40]
total_sum=0
for item in number_list:
    total_sum=total_sum+item

print(total_sum)