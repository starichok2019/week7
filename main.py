import os
import platform
import functions
from bank_account import account, exit
from  bank_account import account_f


while True:
    print(functions.display())
    choice = input('Выберите пункт меню')
    if choice == '1':
        name_of_dir = input("Введите имя папки: ")
        os.mkdir(name_of_dir)
    elif choice == '2':
        functions.remove_file_or_dir()
    elif choice == '3':
        functions.copy_file_or_dir()
    elif choice == '4':
        cwd = os.getcwd()
        print(os.listdir(path=cwd))
    elif choice == '5':
        print(functions.print_dirs())
    elif choice == '6':
        print(functions.print_files()
    elif choice == '7':
        print(platform.uname()
    elif choice == '8':
        print(functions.info_about_creator())
    elif choice == '9':
        victory()
    elif choice == '10':
        account()
        account_f()
    if choice == '11':
        new_path = input("Введите путь к желаемой директории: ")
        functions.change_dir(new_path)
    if choice == '12':
        exit()
        functions.save_fails_and_dirs()
    if choice == '13':
        functions.exit()
        break
    else:
        print('Неверный пункт меню.')
