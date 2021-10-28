# -- coding: utf-8 --
n=int(input())
a = []
for i in range(1,n+1):
    i=i**3
    a.append(i)
n=0
for i in a:
    n+=i
print(n)