import os
import shutil
import json


def display():
   print("""
   return        
   Выберите  одно из действий:
   1. создать папку
   2. удалить (файл/папку)
   9. играть в викторину
   10. мой банковский счет
   11. смена рабочей директории
   12. выход    
    """)
   """
   13. хранить содержание рабочей директории в файл  
   14. выход   
   """


def print_dirs():
    pass


def save_fails_and_dirs():
    with open("listdir.txt", 'w') as f:
        f.write("files: ")
        for file in print_files():
            f.write(file)
            f.write(" ")
        f.write("\ndirs: ")
        for dir in print_dirs():
            f.write(dir)
            f.write(" ")


def remove_file_or_dir():
    cwd = os.getcwd()
    while True:
        print("""
                Вы берите одно из действий:
                1. удалить папку
                2. удалить файл
                3. вернуться в главное меню
                """)
        choice = input("Выбранное действие: ")
        if choice == '1':
            name_of_dir = input("Введите имя папки: ")
            if name_of_dir in os.listdir(path=cwd):
                shutil.rmtree(name_of_dir)
                print("Папка успешно удалена.")
                break
            else:
                print("В вашей директории нет папки с таким именем.")

        if choice == '2':
            name_of_file = input("Введите имя файла: ")
            if name_of_file in os.listdir(path=cwd):
                os.remove(name_of_file)
                print("Файл успешно удален.")
                break
            else:
                print("В вашей директории нет файла с таким именем.")

        elif choice == '3':
            break
        else:
            print('Неверный пункт меню')


def copy_file_or_dir():
    cwd = os.getcwd()
    while True:
        print("""
                Выберите одно из действий:
                1. копировать папку
                2. копировать файл
                3. вернуться в главное меню
            """)
        choice = input("Выбранное действие:")
        if choice == '1':
            src = input("Введите имя папки-источника: ")
            dst = input("Введите имя папки-приемника: ")
            if src in os.listdir(path=cwd) and dst not in os.listdir(path=cwd):
                shutil.copytree(src, dst)
                print("Папка успешно скопирована.")
                break
        else:
            print("Проверте отсутствие папки-приемника и сущеование папки источника.")


        choice = input("Выбранное действие:")
        if choice == '2':
            src = input("Введите имя файла- источника: ")
            dst = input("Введите имя файла-приемника: ")
            if src in os.listdir(path=cwd):
                shutil.copyfile(src, dst)
                print("Файл успешно скопирован.")
                break
            else:
                print("В вашей директории нет файла с таким именем.")
        if choice == '3':
            break
        else:
            print('Неверный пункт меню.')


def ptint_dirs():
    cwd = os.getcwd()
    onlydirs = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]
    return onlydirs

def print_files():
    cwd = os.getcwd()
    onlyfiles = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    return onlyfiles
def info_about_creator():
    return" This program was written by Boris Shustrov"


def change_dir(new_path):
    if not os.path.isabs(new_path):
        new_path = os.path.join(r'C\Users' , new_path)
    os.chdir(new_path)

def exit():
    print("Спасибо за пользование нашими услугами")





