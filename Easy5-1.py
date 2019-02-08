# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys

def dir_create():
    for i in [os.path.join(os.getcwd(), 'dir_' + str(i + 1)) for i in range(9)]:
        try:
            os.mkdir(i)
            print(i, 'создана')
        except OSError:
            print(i, 'существует')


dir_create()


def dir_delete():
    ddel = ''
    while ddel not in {'y', 'Y', 'n', 'N'}:
        ddel = input('Удалит с dir_1 по dir_9 [y/n]?')

    if ddel in ['Y', 'y']:
        for i in [os.path.join(os.getcwd(), 'dir_' + str(i + 1)) for i in range(9)]:
            try:
                os.rmdir(i)
                print(i, 'удалена')
            except OSError:
                print('Ошибка при удалении')


dir_delete()
