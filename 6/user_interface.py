import data_prov as dp
file_input = "Sprav.txt"

menuitems = [
    ("1", "Показать все записи"),
    ("2", "Найти запись"),  
    ("3", "Добавить новый контакт"),
    ("4", "Удалить контакт"),
    ("5", "Изменить контакт"),
    ("6", "Выход")]
        
def menu(menuitems):
    for i in menuitems:
        print(i[0],i[1])

menu(menuitems)

text_menu = input('Введите номер меню:  ')
if text_menu == '1':
    dp.viewFile(file_input)
elif text_menu == '2': 
    dp.findUser(file_input)
elif text_menu == '3':
    dp.writeFile(file_input)
elif text_menu == '4':
    dp.del_data(file_input)
elif text_menu == '4':
    dp.change_data(file_input)
elif text_menu == '6':
    lambda: exit(file_input)


# цикл ?

