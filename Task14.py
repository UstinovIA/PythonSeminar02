# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

limit = int(input("Введите число N: "))
current_value = 2
while current_value <= limit:
    print(current_value)
    current_value *= 2