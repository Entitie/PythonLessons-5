# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
import sys


def file_copy():
    print('Копия файла создана -', shutil.copyfile(sys.argv[0], sys.argv[0]+'.copy'))


file_copy()
