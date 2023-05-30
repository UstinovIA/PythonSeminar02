# x+y=sum xy=multi x=multi/y y+multi/y=sum y^2+multi=sum*y 
# y^2-sum*y+multi=0

sum = int(input("Введите сумму загаданных чисел: "))
multi = int(input("Введите произведение загаданных чисел: "))
D = sum * sum - 4 * multi
first_number = (sum + D)/2
second_number = (sum - D)/2
print(f"Загаданные числа: {first_number} и {second_number}")
# y^2-15y+50=0
# D=225-24=1
# 5+1/2=3 5-1/2=2