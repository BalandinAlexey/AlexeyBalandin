# -- coding: utf-8 --
print('Введите количество чисел')
n=int(input())
a = []
print('Укажите каждое из этих чисел')

for i in range (0,n):
    a.append(int(input()))
n=0

for i in a:
    n+=i
print(n)