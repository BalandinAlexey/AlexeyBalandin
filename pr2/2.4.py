# -- coding: utf-8 --
a = int(input('Введите расстояние между рядами: '))
b = int(input('Введите расстояние между дырочками: '))
l = int(input('Введите длину свободного конца шнурка: '))
N = int(input('Введите количество дырочек в ряду: '))

def c(_a, _b, _l, _N):
    sum = 0

    sum += _a/2
    for i in range(_N-1):
        sum += _b+_a
    return sum

print(c(a, b, l, N))