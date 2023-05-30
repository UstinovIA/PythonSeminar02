# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

count_coins = int(input("Введите количество монет: "))
count_up_side = 0
count_down_side =0
for i in range(count_coins):
    temp = random.randint(0,1)
    if temp == 0:
        count_up_side+=1
    else:
        count_down_side+=1
if count_up_side > count_down_side:
    print(f"Необходимо перевернуть {count_down_side} монет")
else:
    print(f"Необходимо перевернуть {count_up_side} монет")