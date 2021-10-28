f1=1
f2=1
 
n = int(input())
k=int(input())
 
print(f1, f2, end=' ')
 
for i in range(k, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')