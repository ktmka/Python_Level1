from menu import Menu
import function as fn

#меню - список из кортежей
#в каждом кортеже метка пункта меню, название пункта меню, и функция

if __name__ == "__main__":
    menuitems = [
        ("1", "Вывод автобуса", fn.print_all_data),
        ("2", "Добавление автобуса", fn.add_data),
        ("3", "Вывод водителей", fn.search_data),
        ("4", "Добавление водителей", fn.del_data),
        ("5", "Вывод маршрута", fn.edit_data),
        ("6", "Добавление маршрута", fn.edit_data),
        ("7", "Выход", lambda: exit())]
        
menu = Menu(menuitems)     
# fn.clear_screen()
menu.run(">>>>>")