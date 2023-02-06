# data = open('Sprav.txt', 'w+')  
# data.writelines("hello")   

# data = open('Sprav.txt', 'r+')
# data.writelines("hello" + "\n")   #работает запись в режиме чтения только с параметром +
# #перезапись в конец файла
# # \n - перенос строки

# print(data.readlines())
# # readlines/readline  - чтение всех строк/одной строки

# data.close()

# ----------------------------------------------------------------------
file_input = "Sprav.txt"
text_1 = "Petrov222"

def writeFile(file_name, text_1):
    with open(file_name, "a+") as data:   
        # r+ - перезапись одной строки (первой),  a+ - добавление в конец файла 
        #                                         без перезаписи и ЧТЕНИЕ
        data.writelines(text_1 + "\n")
        
writeFile(file_input, text_1)
   
def readFile(file_name):
    result = []
    # прочитали файл и вернули список (превратили в список текст из этого файла):
    with open(file_name, "r+") as data:
        for line in data:
            result.append(line.split())   #разбиваем на отдельные объекты (ФИО+телефон) по строкам
    return result
#или прочитали файл и вернули просто текст (str) из этого файла:
        # return data.read()    #readline - чтение одной строки, read - всего файла



# именованные и позиционные параметры
# именованный параметр для функции:    
# print(readFile(file_name = file_input))
# или позиционный параметр для функции:  

print(readFile(file_input))
print(type(readFile(file_input)))  #определяем класс
# получаем одно и то же

#поиск в телефонной книге - парсим список:
# def findUser(users_list):
#     find_name = "Ivan,"
#     for name in users_list:
#         if name[1] == find_name:
#             print(name[3])
    
# findUser(readFile(file_input))

#Важно: если есть пустые строки в файле - это может вызвать ошибку


