# values = [1,2,3,4,5,6,7]
# transformation = lambda x:x**2
# transformed_value = list(map(transformation, values))
# print(transformed_value)

# Задача 49. Самая далекая планета (макс.орбита в списке)
orbits = [(1,3), (2.5,10),(7,2),(6,6),(4,3)]
from math import pi
# 6.6 - круговая орбита, ее исключаем
# def findOrbit(orbits):
#     Smax = 0
#     index = 0
#     listS = []
#     def square(a,b):
#         return pi * a * b
#     for i in range(len(orbits)):
#         x = orbits[i][0]
#         y = orbits[i][1]
#         if (x != y):
#             if (square(x,y) > Smax):
#                 Smax = square(x,y)
#                 index = i
#     listS.append(square(x,y))
#     return(orbits[index], Smax)
# print(findOrbit(orbits))
            
# Короткая запись 
# def findOrbit(orbits):
#     resList = [i for i in orbits if i[0] != i[1]]
#     areaList = [(pi * i[0] *i[1]) for i in resList]
#     maxAreaIndex = areaList.index(max(areaList))
#     return resList[maxAreaIndex]
    
# print(findOrbit(orbits))

# def findOrbit(orbits):
#     resList = [i for i in orbits if i[0] != i[1]]   #выражение if - аналог фильтра
#     print("только эллиптичские", resList)
#     areaList = [(pi * i[0] *i[1]) for i in resList]
#     print("список площадей", areaList)
#     maxAreaIndex = areaList.index(max(areaList))
#     print(maxAreaIndex)
#     return resList[maxAreaIndex]
    
# print(findOrbit(orbits))

#или воспользуемся фильтром вместо if
# def findOrbit(orbits):
#     resList = list(filter(lambda x: x[0] != x[1], orbits))   #сохраняем результат фильтра в список
#     print("только эллиптичские", resList)
#     areaList = [(pi * i[0] *i[1]) for i in resList]
#     print("список площадей", areaList)
#     maxAreaIndex = areaList.index(max(areaList))
#     print(maxAreaIndex)
#     return resList[maxAreaIndex]
    
# print(findOrbit(orbits))

# -------------------------------------------
# Задача  --- Выдать фразу same если  результаты преобразования каждого элемента в списке одинаковые
values = [3,6,12,15]

# def same_1(x, arrays):   #есть функция same_1
#     for i in arrays:
#         if x(i):
#             return False   #то есть 0, результат действия
#     return True            #то есть 1

#другой вариант 
def same_1(x, arrays):   #есть функция same_1
    return len(set(map(x, arrays))) == 1



#запустим ее с условием
if same_1(lambda x:x % 3, values):  #где x = lambda x:x%2, то есть каждое значение %2. Если выполняется = true
    print("same")
else:
    print("different")
    

    