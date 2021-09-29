# -- coding: utf-8 --
n = int(input('Введите минуты: '))
h = 0
while n>59:
    h += 1
    n -= 60
    if h==24:
        h=0

if h<10:
    h = '0' + str(h)

if n<10:
    n = '0' + str(n)
    
print('Время', h, ':', n)