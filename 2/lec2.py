# def fact(n):
#     result = 1
#     while (n > 1):
#         result *= n
#         n -= 1
#     return result
    
# n = int(input())
# print(fact(n))

# def fibonacci(n):
#     # дано натуральное число, нужно проверить его номер (индекс) в ряду фибоначчи
#     # 0 1 1 2 3 5 8 - ряд фибоначчи
#     # 1 2 3 4 5 6 7  - нумерация (индексы в ряду)
#     if (n == 0):
#         return 1
#     if (n == 1):
#         return 2,3
#     number0 = 0
#     number1 = 1
#     count = 2
#     while (n >= number1):
#         if (n == number1):
#             return count
#         temp = number1
#         number1 += number0
#         number0 = temp
#         count += 1
#     return -1

# n = int(input())
# print(fibonacci(n))

#какая последовательность положительных чисел в ряду самая длинная
import random
# n = 20
# m = []    #list
# count = 0
# max = 0
# for i in range(0, n):
#     random_num = round(random.randint(-50, 50),0)
#     m.append(random_num) 
    
#     if (m[i] > 0):
#         count += 1
#         if (max < count): max = count
#     else: count = 0
# print(n)       
# print(m)
# print(max)

# def arbuzLine(n):
#     arbuz = []
#     for i in range(n):
#         arbuz.append(random.randint(5000, 30000))
#     return arbuz

# n = int(input())

# arbuz = arbuzLine(n)
# print(arbuz)
# min = max = arbuz[0]
# for i in arbuz:
#     if max > i: max = i
#     if min < i: min = i
# print(min)
# print(max)


while True:
    try:
        num = int(input('введите трехзгачное число: '))
        if 99 < num and num < 1000:
            print(f'сумма цифр: {num // 100 + num // 10 % 10 + num %10}')
            break
        else: print('это не трехзначое число, попробуйте еще раз')
    except:
        print('некорректный ввод, попробуйте еще раз')
        