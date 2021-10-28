# -- coding: utf-8 --
n=int(input())
s=1
c=1

for i in range(2,n+1):
    c*=i
    s+=c

print(s)