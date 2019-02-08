# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os


def dir_info():
    print('Папки в катологе:\n' + '\n'.join([i for i in os.listdir(os.getcwd()) if os.path.isdir(i)]))


dir_info()
