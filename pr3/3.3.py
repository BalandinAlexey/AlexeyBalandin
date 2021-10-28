# -- coding: utf-8 --
import sys
a=int(input())
b=int(input())
if a<=b:
    print('Введите первое число большее второму')
    sys.exit()


if (a%2 == 0) and (b%2 == 0):                             #Если оба числа чётные
    print('Нечётные Числа: ')
    for i in range(a-1,b,-2):
        print(i)


if (a%2 != 0) and (b%2 != 0):                             #Если оба числа нечётные
    print('Нечётные Числа: ')
    for i in range(a,b-1,-2):
        print(i)


if (a%2 == 0) and (b%2 != 0):                             #Если только первое число чётное
    print('Нечётные Числа: ')
    for i in range(a-1,b-1,-2):
        print(i)


if (a%2 != 0) and (b%2 == 0):                             #Если только второе число чётное
    print('Нечётные Числа: ')
    for i in range(a,b,-2):
        print(i)