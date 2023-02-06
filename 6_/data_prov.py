# - Чтение файла - вспомогательная функция не для пользователя
def readFile(file_name):
    result = []
    # прочитали файл и сделали из него список:
    with open(file_name, "r+") as data:
        for line in data:
            temp = line.replace(',',"")   #убираем запятые чтобы не путаться при вводе для поиска
            temp = temp.lower()
            result.append(temp.split())   #разбиваем список на отдельные объекты-подсписки (записи) 
    return result

# - Показать все записи, для пользователя
def viewFile(file_name):
    result = []
    with open(file_name, "r", encoding="utf8") as data:
        for line in data:
            result.append(line.strip('\n').split(',')) 
        for i in result:
            print(i[0],i[1],i[2], i[3])   #убираем скобки и запятые в выводе
    
#--------------------------------------------------------
# - Добавить новый контакт
def writeFile(file_name):
    last_name = input("Укажите фамилию: ")
    first_name = input("Укажите имя: ")
    surname = input("Укажите отчество: ")
    phone = input("Укажите номер телефона: ")
    new_contact = [last_name, first_name, surname, phone]  #собираем в список
    new_contact = ", ".join(new_contact) + "\n"            #преобразуем список в строку для записи
    new_contact = new_contact.lower()
    with open(file_name, "a+", encoding='utf-8') as data:  
        data.writelines(new_contact)
    print(f"Отлично! Записан новый контакт: {new_contact}")
    

#--------------------------------------------------------
# - Найти запись 
def findUser(file_name):
    find_name = input("Введите имя (возврат - Enter):  ")
    find_name = find_name.lower()
    if find_name == '':
        return
        #возврат в меню
    flag = 1
    users_list = readFile(file_name)  #формируем подсписки (записи)
    for name in users_list:   #перебор подсписков (записей) в общем списке Sprav.txt
        if find_name in name:
            flag = 0
            print(f"Найдена запись: {name}")
            command = input("Введите значение: 1 - удалить запись, 2 - изменить запись, любая клавиша - возврат.   ")
            if command == '1':
                del_index = users_list.index(name)
                del users_list[del_index:del_index + 1]
                print(f"Удалена запись {name}")
                new_data = ""     
                for name in users_list:
                    str_name = ", ".join(name) + "\n"
                    new_data += str_name
        
                with open(file_name, "w", encoding="utf8") as datafile:
                    datafile.write(new_data)
            elif command == '2':
                name_index = users_list.index(name)
                print("Какую часть записи вы хотите изменить?")
                last_name = input("Укажите фамилию: ")
                last_name = last_name.lower()
                first_name = input("Укажите имя: ")
                first_name = first_name.lower()
                surname = input("Укажите отчество: ")
                surname = surname.lower()
                phone = input("Укажите номер телефона: ")
                users_list[name_index] = [last_name, first_name, surname, phone]  #собираем в список
                print(f"Изменена запись: {name} на {users_list[name_index]}")
                new_data = ""     
                for name in users_list:
                    str_name = ", ".join(name) + "\n"
                    new_data += str_name
        
                with open(file_name, "w", encoding="utf8") as datafile:
                    datafile.write(new_data)

            else:
                return
   
    if flag:
        print(f"'{find_name}' не найдено")  
        
  
#---------------------------------------------------------------          
#Удаление записи

def del_data(file_name):
    find_name = input("Введите имя (возврат - Enter):  ")
    find_name = find_name.lower()
    if find_name == '':
        return 
        #возврат в меню
    
    users_list = readFile(file_name)  #формируем подсписки (записи)
    for name in users_list:   #перебор в общем списке Sprav.txt
        if find_name in name:
            del_index = users_list.index(name)
            del users_list[del_index:del_index + 1]
            print(f"Удалена запись {name}")
    new_data = ""     
    for name in users_list:
        str_name = ", ".join(name) + "\n"
        new_data += str_name
        
    with open(file_name, "w", encoding="utf8") as datafile:
        datafile.write(new_data)


#-------------------------------------------------------
#Изменение записи

def change_data(file_name):
    find_name = input("Введите имя (возврат - Enter):  ")
    find_name = find_name.lower()
    if find_name == '':
        return 
        #возврат в меню
    
    users_list = readFile(file_name)  #формируем подсписки (записи)
    for name in users_list:   #перебор в общем списке Sprav.txt
        if find_name in name:
            name_index = users_list.index(name)
            print("Какую часть записи вы хотите изменить?")
            last_name = input("Укажите фамилию: ")
            last_name = last_name.lower()
            first_name = input("Укажите имя: ")
            first_name = first_name.lower()
            surname = input("Укажите отчество: ")
            surname = surname.lower()
            phone = input("Укажите номер телефона: ")
            users_list[name_index] = [last_name, first_name, surname, phone]  #собираем в список
            print(f"Изменена запись: {name} на {users_list[name_index]}")
    new_data = ""     
    for name in users_list:
        str_name = ", ".join(name) + "\n"
        new_data += str_name
        
    with open(file_name, "w", encoding="utf8") as datafile:
        datafile.write(new_data)



# #-------------------------------------------------------------------
# #Важно: если есть пустые строки в файле - это может вызвать ошибку
# Сделать удаление пустых строк
# Убрать повторяющиеся функции (разбить крупные на более мелкие или заменить циклами)
# Обработка исключений
# Настроить форматирование при выводе записей

