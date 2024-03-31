from os.path import isfile
from os import remove


def build_note(text, name):
    with open(f"{name}.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Заметка {name} создана.")


# создание
def create_note():
    name = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    build_note(text, name)


# чтение
def read_note(name):
    if isfile(f"{name}.txt"):  # проверяем, существует ли файл
        try:
            with open(f"{name}.txt", encoding="utf-8") as file:
                text = file.read()
        # Добавляем возможность чтения файлов из "блокнота" Windows
        except:
            with open(f"{name}.txt", encoding="cp1251") as file:
                text = file.read()            
        print(f'Текст заметки: {text}')
    else: 
        print('Заметка не найдена.')


# изменение
def edit_note(name):
    if isfile(f"{name}.txt"):  # проверяем, существует ли файл
        # Читаем  и выводим на экран
        print('Старый', end = ' ')
        read_note(name)
        # Перезаписываем файл
        with open(f"{name}.txt", "w", encoding="utf-8") as file:
            text = input('Введите новый текст: ')
            file.write(text)
        # Выводим на экран перезаписанный файл
        print('Новый', end = ' ')
        read_note(name)
        print('Текст заметки успешно перезаписан.')
    else: 
        print('Заметка не найдена.')


# удаление     
def delete_note(name):    
    if isfile(f"{name}.txt"):  # проверяем, существует ли файл
        thirst_for_deletion = input(
            "\nВы действительно хотите удалить файл?\n"
            "Если да, введите  'da', если нет - то произвольные символы: "
            )
        if thirst_for_deletion == 'da':
            remove(f"{name}.txt")
            print('Заметка удалена!')
        else:
            print('Удаление отменено. Возврат в Основное Меню.')    
    else: 
        print('Заметка не найдена.')


# основной код
def main():
    while True:
        menu = {
            '1': 'create_note',
            '2': 'read_note',
            '3': 'edit_note',
            '4': 'delete_note',
        }
        print('')   # добавляем одиночный отступ
        
        # Вывод меню на экран
        for k in sorted(menu.keys()):
            print(f'{k} : {menu.get(k)}')
        
        # Выбор операции
        key = input('\nВведите ключ операции. \
Если хотите выйти, введите произвольные символы или пустоту: ').strip()

        if key == '1' or key == '2' or key == '3' or key == '4':
            print(f'Выбрана операция: {menu[key]}\n')
        # Вызов соответствующей операции или завершение программы        
        operation = menu.get(key)
        if operation:
            print(f'Выбрана операция: {operation}\n')
            note_name = input("Введите название заметки: ")
            globals()[operation](note_name)
        else:
            print('Работа программы завершена.\n')
            break

        # Вызов соответствующей операции или завершение программы
        if key == '1':
            create_note(note_name)
        elif key == '2':
            read_note(note_name)
        elif key == '3':
            edit_note(note_name)
        elif key == '4':
            delete_note(note_name)