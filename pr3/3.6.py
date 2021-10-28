# -- coding: utf-8 --
n=int(input())
a = []
for i in range(1,n+1):
    a.append(i)
n=1
for i in a:
    n*=i
print('Факториал значения: ', n)