# Задача №25

# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется 
# к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# numText = 'a a a b c a a d c d d'
# numText = numText.split()
# print(numText)      #результат в виде массива

# numText = 'a a a b c a a d c d d'
# array = numText.split()
# print(array)
# # print(numNewText)      #результат в виде массива

# data = {}
# res = ''
# for i in array:
#     if i in data:
#         data[i] += 1
#         res += i + '_' + str(data[i]) + ' '
#     else:
#         data[i] = 0
#         res += i + " "
#     print(res)



# Задача №27

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

st = "She sells sea shells on the sea shore;\
    The shells that she sells are sea shells I'm sure.\
    So if she sells sea shells on the sea shore, \
    I'm sure that the shells are sea shore shells"
# st = st.replace(";"," ").replace(","," ").replace("."," ")
st = st.lower()
st = st.replace(";"," ")
st = st.replace(","," ")
st = st.replace("."," ")
word = set(st.split())   #по умолчанию split с пробелами
print(word)
print(len(word))

# Задача №29

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)

# Решение
# n = int(input("Введи число  "))
# if (n !=0): 
#     max = n
#     while n != 0:
#         if max < n: max = n
#         n = int(input("Введи следующее число  "))
#     print(max)
# else:
#     print("числа отсутствуют")

