import random

# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# n = int(input("Введите количество элементов в массиве: "))
# X = int(input("Введите число, которое нужно проверить: "))
# array = []
# for num in range (0, n):
#     array.append(round(random.randint(1, round(n/2))))  #округление n/2 для исключения дробных значений для нечетных n
# count = 0
# for i in range (0, len(array)):     
#     if array[i] == X: count += 1
# print(f"число {X} встречено {count} раз(a) в массиве {array}")
# -----------------------------------------------------------------------

# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# n = int(input("Введите количество элементов в массиве: "))
# x = int(input("Введите число, для которого ищем самый близкий элемент: "))
# array = []
# for num in range (0, n):
#     array.append(round(random.randint(1, n)))  
# print(array)
# min = abs(x - array[0])
# find = array[0]
# for i in range (1, len(array)):
#     if (abs(array[i] - x) <= min): 
#         min = abs(array[i] - x)
#         find = array[i]
# print(find)   
    
# -------------------------------------------------------------
# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо 
# только английские, либо только русские буквы.

# вариант: ключ => кол-во очков, значения => буквы, т.к.значений букв больше чем очков
inpDict = {1:'АВЕИНОРСТAEIOULNSTR', 2:'ДКЛМПУDG', 3:'БГЁЬЯBCMP', 4:'ЙЫFHVWY', 5:'ЖЗХЦЧK', 8:'ШЭЮJX', 10:'ФЩЪQZ'} 
countWord = input("Введите слово:   ")
countWord = countWord.upper()
count = 0
for letter in countWord:           #пробегаемся по буквам в слове
    for i in inpDict:             #пробегаемся по ключам словаря (i)
        if letter in inpDict[i]:    #пробегаемся значениям словаря inpDict[i]
            count = count + i
if (count > 0): print(count)
else: print("таких букв в словаре нет")
