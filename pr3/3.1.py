# -- coding: utf-8 --
a=int(input())
b=int(input())
if a <= b:
    for i in range(a,b+1):
        print(i)
else:
    print('Ошибка: первое число должно быть меньше второго')