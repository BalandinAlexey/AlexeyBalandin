# -- coding: utf-8 --
s=[]
a1=1
a2=1
n=int(input())
s.append(a1)
s.append(a2)

for i in range (2,n):
    a1,a2=a2,a1+a2
    s.append(a2)

n=0

for i in s:
    n+=i
print(n)
