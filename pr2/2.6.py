# -- coding: utf-8 --
ai = int(input('Введите строку первой клетки: '))
aj = int(input('Введите столбец первой клетки: '))
bi = int(input('Введите строку второй клетки: '))
bj = int(input('Введите столбец второй клетки: '))

if ai<1 or aj<1 or bi<1 or bj<1:
    print('Некоректно введены данные')
    quit()

if ((ai + aj)%2==(bi + bj)%2):
    print('Да')
else:
    print('Нет')
