# Задача 10 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
import random
# n = int(input("Введите количество монет: "))
# m = []    #list
# countFor0 = 0
# countFor1 = 0
# for i in range(0, n):
#     random_num = round(random.randint(0, 1),0)
#     m.append(random_num) 
#     if (m[i] > 0):
#         countFor1 += 1
#     else: countFor0 += 1
# print(m) 
# print(countFor1)       
# print(countFor0)
# if countFor1 > countFor0:
#     print(f'нужно перевернуть  {countFor0} монет(ы)')
# else: print(f'нужно перевернуть  {countFor1} монет(ы)')
    
# -------------------------------------------------------------
# Задача 12 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Решение:
# x + y = S  сумма
# y = S-x
# x * y = P  произведение
# x * (S-x) = P   подставим выражение (S-x) вместо y
# раскроем скобки:
# -x*x + S*x = P    
# перенесем P влево и приведем к виду кв.уравнения ax2 + bx + c = 0:
# -x*x + S*x - P = 0
# Дискриминант D = S*S - 4*(-1)*(-P)
#              D = S*S - 4*P

S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))
from math import sqrt
D = S*S - 4*P  
if D > 0:  # D > 0 => два корня уравнения
    koren = sqrt(D)/2
    h = S/2
    num1 = int(h - koren)
    num2 = int(h + koren)
    if (num1 + num2 == S and num1 * num2 == P):
        print(f'это числа {int(num1)} и {int(num2)}')
    else: print("решения нет")
elif D == 0: # D = 0 => один корень
    num1 = S/2
    num2 = num1
    if (num1 + num2 == S and num1 * num2 == P):
        print(int(num1), int(num2))
    else: print("решения нет")
else: print("решения нет")


# -------------------------------------------------------------
# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# N = int(input("Введите число: "))
# if N > 0:
#     k = 0
#     num = 2
#     while (num ** k <= N):
#         print(int(num ** k))
#         k += 1
# else: print("ответа нет")