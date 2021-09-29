# -- coding: utf-8 --
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

def _min(a, b, c):
    if(a<b and a<c):
        return a
    if(b<a and b<c):
        return b
    if(c<b and c<a):
        return c

print(_min(a, b, c))