# Задача 2. Найдите сумму цифр трехзначного числа.
x = int(input("введите трехзначное число"))
if (99 > x > 1000):
    result = 0
    while (x > 0):
        result += x % 10
    print(result)
else: 
    print("это число не трехзначное")
